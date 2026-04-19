from openai import OpenAI

def extract_tasks(text, api_key):
    client = OpenAI(api_key=api_key)

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

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300
    )

    return response.choices[0].message.content


# =========================
# 🔹 Run Program
# =========================
if __name__ == "__main__":
    api_key = input("Enter OpenAI API Key: ")

    print("\nPaste your meeting text (press Enter twice to finish):\n")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    meeting_text = "\n".join(lines)

    print("\n🧠 Extracting Tasks...")
    tasks = extract_tasks(meeting_text, api_key)

    print("\n📌 Action Items:")
    print(tasks)