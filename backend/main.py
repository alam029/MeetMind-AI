import time
import sounddevice as sd
from scipy.io.wavfile import write
import whisper
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# =========================
# 1. JOIN GOOGLE MEET
# =========================
def join_meet(meet_link):
    options = webdriver.ChromeOptions()
    options.add_argument("--use-fake-ui-for-media-stream")  # auto allow mic/cam

    driver = webdriver.Chrome(options=options)
    driver.get(meet_link)

    time.sleep(10)

    try:
        # Turn off mic
        driver.find_element(By.XPATH, '//div[@aria-label="Turn off microphone"]').click()
    except:
        pass

    try:
        # Turn off camera
        driver.find_element(By.XPATH, '//div[@aria-label="Turn off camera"]').click()
    except:
        pass

    time.sleep(5)

    try:
        # Click Join button
        driver.find_element(By.XPATH, '//span[text()="Join now"]').click()
    except:
        print("Join button not found")

    print("✅ Joined Meeting")
    return driver


# =========================
# 2. RECORD AUDIO
# =========================
def record_audio(filename="meeting.wav", duration=60):
    fs = 44100
    print("🎤 Recording started...")

    audio = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()

    write(filename, fs, audio)
    print("✅ Recording saved:", filename)


# =========================
# 3. TRANSCRIBE AUDIO
# =========================
def transcribe_audio(file):
    print("🧠 Loading Whisper model...")
    model = whisper.load_model("base")

    print("✍️ Transcribing...")
    result = model.transcribe(file, fp16=False)

    print("\n📄 Transcript:\n")
    print(result["text"])

    return result["text"]


# =========================
# MAIN PIPELINE
# =========================
if __name__ == "__main__":
    MEET_LINK = "https://meet.google.com/your-link-here"

    # Step 1: Join meeting
    driver = join_meet(MEET_LINK)

    # Wait for meeting to stabilize
    time.sleep(10)

    # Step 2: Record audio
    record_audio("meeting.wav", duration=60)

    # Step 3: Transcribe
    text = transcribe_audio("meeting.wav")

    # Close browser
    driver.quit()