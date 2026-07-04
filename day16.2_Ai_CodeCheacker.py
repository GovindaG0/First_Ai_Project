from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found")

client = genai.Client(api_key=api_key)


def code_checker(code):
    chat = client.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction="""
You are an expert Code Reviewer.

Analyze the code and provide:

1. Code Quality (/10)
2. Bugs
3. Improvements
4. Best Practices
5. Optimized Code (if required)

Explain everything in beginner-friendly language.
""",
            temperature=0.2
        )
    )

    response = chat.send_message(code)

    print("\n========== Code Review ==========")
    print(response.text)


def main():
    while True:
        print("\nPaste your code (type END on a new line to finish or EXIT to quit):")

        lines = []

        while True:
            line = input()

            if line.upper() == "EXIT":
                return

            if line.upper() == "END":
                break

            lines.append(line)

        code = "\n".join(lines)

        code_checker(code)


main()