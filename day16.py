from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents="Explain Python functions with an example."
# )

# print(response.text)

# =====================System Instructions=================

# from google.genai import types
# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents="Explain loops.",
#     config=types.GenerateContentConfig(
#         system_instruction="You are an expert Python trainer who explains concepts with beginner-friendly examples.",
#          max_output_tokens=250,
#         temperature=0.2
#     )
# )

# print(response.text)

#================================= taking dynamic input=====================
# content=input("Enter Your question ")
# response=client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents=content
# )
# print(response.text)

# ===============================Chat History=================

from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat = client.chats.create(model="gemini-2.5-flash")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    response = chat.send_message(question)

    print("\nGemini:")
    print(response.text)