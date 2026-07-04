from google import genai
from dotenv import load_dotenv
from google.genai import types
import os

load_dotenv()
try:
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
except Exception as e:
    print(e)

def emailGenarator(email):
    chat=client.chats.create(model="gemini-2.5-flash",
                             config=types.GenerateContentConfig(
                                 system_instruction="Your an Profrssional Email writer user will provide porpose , recipent and reson of mail you need to write email base on that example if it is for office work  it should be profession email and same for casual and formal",
                                max_output_tokens=2500,
                                
                             ))

    response=chat.send_message(email)
    print("\n Your Email")
    print(response.text)       


def main():
    print("===== AI Email Writer =====")

    purpose = input("Purpose: ")
    recipient = input("Recipient: ")
    reason = input("Reason: ")

    prompt = f"""
Purpose: {purpose}
Recipient: {recipient}
Reason: {reason}
"""
    emailGenarator(prompt)

main()
