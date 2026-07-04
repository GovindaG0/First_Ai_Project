from google import genai
from dotenv import load_dotenv
from google.genai import types
import os

load_dotenv()
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# ===========Python trainer==========

def Pyhton_Trainer(question):
    chat = client.chats.create(model="gemini-2.5-flash",
                           config=types.GenerateContentConfig(
        system_instruction="You are an expert Python trainer who explains user input  concepts with beginner-friendly examples.",
        #  max_output_tokens=1000,
        temperature=0.2
    )
                           )
    response = chat.send_message(question)

    print("\nPython Trainer:")
    print(response.text)

# =================Java Trainer==============

def java_Trainer(question):
    chat=client.chats.create(model="gemini-2.5-flash",
                             config=types.GenerateContentConfig(
                                 system_instruction="You are an expert Java trainer who explains user input  concepts with beginner-friendly examples.",
                                 temperature=0.2,
                                #  max_output_tokens=1000
                             )
                             )
    response=chat.send_message(question)
    print("\nJava Trainer ")
    print(response.text)

# ==================AS400 TRAINER===============

def as400_Trainer(question):
    chat=client.chats.create(model="gemini-2.5-flash",
                             config=types.GenerateContentConfig(
                                 system_instruction="You are an expert As400 trainer who explains user input  concepts with beginner-friendly examples.",
                                 temperature=0.2,
                                #  max_output_tokens=1000
                             ))
    response=chat.send_message(question)
    print("\nAs400 Trainer")
    print(response.text)

def main():
    while True:
        print("1. Python Trainer ")
        print("2. Java Trainer ")
        print("3. As400 Trainer")
        print("4: exit")
        option=int(input("Choose Your Trainer "))
        if option==1:
            while True:
                question=input("\nYou ")
                if question.lower()=="exit":
                    break
                Pyhton_Trainer(question)
        elif option==2:
            while True:
                question=input("\nYou ")
                if question.lower()=="exit":
                    break
                java_Trainer(question)
        elif option==3:
            while True:
                question=input("\nYou ")
                if question.lower()=="exit":
                    break
                as400_Trainer(question)
        else:
            break

main()
        



        

                           
