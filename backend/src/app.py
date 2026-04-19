"""Unified backend app for MeetMind AI.

This file merges the existing backend utility scripts into one place:
- Google Meet join + audio recording
- Whisper transcription
- OpenAI summary generation
- OpenAI task extraction
- SMTP mail sending
"""

from __future__ import annotations

import smtplib
import ssl
import time
from dataclasses import dataclass
from email.message import EmailMessage
from pathlib import Path

import sounddevice as sd
import whisper
from openai import OpenAI
from scipy.io.wavfile import write
from selenium import webdriver
from selenium.webdriver.common.by import By


@dataclass(slots=True)
class AppConfig:
    openai_api_key: str
    sender_email: str | None = None
    sender_password: str | None = None
    smtp_server: str = "smtp.gmail.com"
    smtp_port: int = 587


class MeetMindApp:
    def __init__(self, config: AppConfig) -> None:
        self.config = config
        self._whisper_model = None
        self._openai_client = OpenAI(api_key=config.openai_api_key)

    def join_meet(self, meet_link: str) -> webdriver.Chrome:
        options = webdriver.ChromeOptions()
        options.add_argument("--use-fake-ui-for-media-stream")

        driver = webdriver.Chrome(options=options)
        driver.get(meet_link)
        time.sleep(5)

        for label in ("Turn off camera", "Turn off microphone"):
            try:
                driver.find_element(By.XPATH, f'//div[@aria-label="{label}"]').click()
            except Exception:
                pass

        time.sleep(2)

        try:
            driver.find_element(By.XPATH, '//span[contains(text(),"Join now")]').click()
        except Exception as exc:
            raise RuntimeError("Join button not found. Check the Meet page UI.") from exc

        print("Joined meeting successfully.")
        return driver

    def record_audio(self, duration: int = 30, filename: str = "meeting_audio.wav") -> str:
        print("Recording audio...")
        sample_rate = 44100
        audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2)
        sd.wait()
        write(filename, sample_rate, audio)
        print(f"Audio saved to {filename}")
        return filename

    def _get_whisper_model(self):
        if self._whisper_model is None:
            self._whisper_model = whisper.load_model("base")
        return self._whisper_model

    def transcribe_audio(self, file_path: str) -> str:
        audio_path = Path(file_path)
        if not audio_path.exists():
            raise FileNotFoundError(f"Audio file not found: {audio_path}")

        print("Transcribing audio...")
        result = self._get_whisper_model().transcribe(str(audio_path))
        return result["text"]

    def summarize_text(self, text: str) -> str:
        prompt = (
            "Summarize the following meeting into short key points.\n\n"
            f"{text}"
        )
        response = self._openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
        )
        return response.choices[0].message.content or ""

    def extract_tasks(self, text: str) -> str:
        prompt = f"""
From the following meeting text, extract only actionable tasks.

Rules:
- Give output in bullet points
- Each task should be clear and short
- Ignore general discussion
- Focus on "who will do what"

Meeting Text:
{text}
"""
        response = self._openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
        )
        return response.choices[0].message.content or ""

    def send_mail(self, receiver_email: str, subject: str, body: str) -> None:
        if not self.config.sender_email or not self.config.sender_password:
            raise ValueError("Sender email and app password are required to send mail.")

        message = EmailMessage()
        message["From"] = self.config.sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message.set_content(body)

        with smtplib.SMTP(self.config.smtp_server, self.config.smtp_port, timeout=30) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(self.config.sender_email, self.config.sender_password)
            server.send_message(message)

        print("Email sent successfully.")

    def process_audio_file(self, file_path: str) -> dict[str, str]:
        transcription = self.transcribe_audio(file_path)
        summary = self.summarize_text(transcription)
        tasks = self.extract_tasks(transcription)
        return {
            "transcription": transcription,
            "summary": summary,
            "tasks": tasks,
        }

    def run_meeting_flow(self, meet_link: str, duration: int = 30) -> dict[str, str]:
        driver = self.join_meet(meet_link)
        try:
            time.sleep(10)
            audio_path = self.record_audio(duration=duration)
            return self.process_audio_file(audio_path)
        finally:
            driver.quit()


def _collect_multiline_input(prompt: str) -> str:
    print(prompt)
    lines: list[str] = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return "\n".join(lines)


def main() -> None:
    print("MeetMind AI Backend")
    print("1. Join meeting and process audio")
    print("2. Process existing audio file")
    print("3. Extract tasks from pasted text")
    print("4. Send email")

    choice = input("Choose an option (1/2/3/4): ").strip()
    openai_api_key = input("Enter OpenAI API Key: ").strip()

    sender_email: str | None = None
    sender_password: str | None = None
    if choice == "4":
        sender_email = input("Enter sender email: ").strip()
        sender_password = input("Enter sender app password: ").strip()

    app = MeetMindApp(
        AppConfig(
            openai_api_key=openai_api_key,
            sender_email=sender_email,
            sender_password=sender_password,
        )
    )

    if choice == "1":
        meet_link = input("Enter Google Meet link: ").strip()
        duration = int(input("Recording duration in seconds: ").strip())
        result = app.run_meeting_flow(meet_link, duration)
        print("\nTranscription:\n", result["transcription"])
        print("\nSummary:\n", result["summary"])
        print("\nTasks:\n", result["tasks"])
    elif choice == "2":
        file_path = input("Enter audio file path: ").strip()
        result = app.process_audio_file(file_path)
        print("\nTranscription:\n", result["transcription"])
        print("\nSummary:\n", result["summary"])
        print("\nTasks:\n", result["tasks"])
    elif choice == "3":
        meeting_text = _collect_multiline_input(
            "\nPaste your meeting text below and press Enter twice to finish:\n"
        )
        tasks = app.extract_tasks(meeting_text)
        print("\nAction Items:\n", tasks)
    elif choice == "4":
        receiver = input("Receiver email: ").strip()
        subject = input("Subject: ").strip()
        body = input("Message: ").strip()
        app.send_mail(receiver, subject, body)
    else:
        raise SystemExit("Invalid option selected.")


if __name__ == "__main__":
    main()
