import time
import sounddevice as sd
from scipy.io.wavfile import write
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# =========================
# 🔹 Join Google Meet
# =========================
def join_meet(meet_link):
    options = webdriver.ChromeOptions()
    options.add_argument("--use-fake-ui-for-media-stream")  # auto allow mic/cam

    driver = webdriver.Chrome(options=options)
    driver.get(meet_link)

    time.sleep(5)

    # Turn off camera (optional)
    try:
        driver.find_element(By.XPATH, '//div[@aria-label="Turn off camera"]').click()
    except:
        pass

    # Turn off mic (optional)
    try:
        driver.find_element(By.XPATH, '//div[@aria-label="Turn off microphone"]').click()
    except:
        pass

    time.sleep(2)

    # Join button
    try:
        join_btn = driver.find_element(By.XPATH, '//span[contains(text(),"Join now")]')
        join_btn.click()
    except:
        print("Join button not found")

    print("✅ Joined Meeting")
    return driver


# =========================
# 🔹 Record Audio
# =========================
def record_audio(duration=30, filename="meeting_audio.wav"):
    print("🎧 Recording audio...")
    fs = 44100  # Sample rate
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()
    write(filename, fs, audio)
    print("✅ Audio saved:", filename)


# =========================
# 🔹 Main
# =========================
if __name__ == "__main__":
    meet_link = input("Enter Google Meet link: ")
    duration = int(input("Recording duration (seconds): "))

    driver = join_meet(meet_link)

    time.sleep(10)  # wait for meeting to stabilize

    record_audio(duration)

    input("Press Enter to leave meeting...")
    driver.quit()