import os
import smtplib
import pandas as pd

from email.message import EmailMessage
from dotenv import load_dotenv
from google import genai

load_dotenv()
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# load sales data 

def load_data(csv_file):
    df=pd.read_csv(csv_file)
    return df.to_string(index=False) 

def genrate_report(data):
    prompt = f"""
You are a senior retail sales analyst.

Analyze this dataset.

{data}

Generate a professional report with:

Executive Summary

Best-selling product

Worst-selling product

Average sales

Products above average

Products below average

Possible customer buying behavior

Business recommendations

Inventory recommendations

Future sales strategy

Format using headings and bullet points.
"""
   
   
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

def sav_repo(report,filename="sales.txt"):
    with open(filename,"w",encoding="utf-8") as file:
        file.write(report)

def main():
    sale_data=load_data("sales.csv")

    report=genrate_report(sale_data)
    print(report)
    sav_repo(report)
main()
    