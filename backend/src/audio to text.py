import whisper

def transcribe_audio(file_path):
    model = whisper.load_model("base")  # small, medium, large available
    
    print("🎧 Processing audio...")
    result = model.transcribe(file_path)
    
    return result["text"]


if __name__ == "__main__":
    path = input("Enter audio file path: ")
    
    text = transcribe_audio(path)
    
    print("\n📝 Transcription:")
    print(text)