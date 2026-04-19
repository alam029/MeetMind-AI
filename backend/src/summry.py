import whisper
from openai import OpenAI

# =========================
# 🔹 Step 1: Audio → Text
# =========================
def audio_to_text(file_path):
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    return result["text"]


# =========================
# 🔹 Step 2: Text → Summary
# =========================
def summarize_text(text, api_key):
    client = OpenAI(api_key=api_key)

    prompt = f"""
    Summarize the following meeting into key points:

    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300
    )

    return response.choices[0].message.content


# =========================
# 🔹 Main
# =========================
if __name__ == "__main__":
    file_path = input("Enter meeting audio file path: ")
    api_key = input("Enter OpenAI API Key: ")

    print("🎧 Converting audio to text...")
    text = audio_to_text(file_path)

    print("\n📝 Full Transcription:")
    print(text)

    print("\n🧠 Generating Summary...")
    summary = summarize_text(text, api_key)

    print("\n📌 Summary:")
    print(summary)