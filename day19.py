import os
import smtplib
import pandas as pd

from email.message import EmailMessage
from dotenv import load_dotenv
from google import genai

load_dotenv()

# -----------------------------
# Gemini Client
# -----------------------------
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


# -----------------------------
# Read Employee Data
# -----------------------------
def load_employee_data(csv_file):
    df = pd.read_csv(csv_file)
    return df.to_string(index=False)


# -----------------------------
# Generate Employee Report
# -----------------------------
def generate_employee_report(employee_data):
    prompt = f"""
You are an HR Analytics Consultant.

Analyze the following employee data.

Provide:

1. Executive Summary

2. Salary Insights

3. Department Analysis

4. Recommendations

Employee Data:

{employee_data}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


# -----------------------------
# Save Report
# -----------------------------
def save_report(report, filename="employee_report.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(report)

    print(f"Report saved as {filename}")


# -----------------------------
# Generate Email
# -----------------------------
def generate_email(report):
    prompt = f"""
Write a professional email to the HR Manager summarizing the following employee report.

Employee Report:

{report}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


# -----------------------------
# Send Email
# -----------------------------
def send_email(subject, body):
    sender = os.getenv("EMAIL")
    password = os.getenv("EMAIL_PASSWORD")
    receiver = os.getenv("RECEIVER_EMAIL")

    msg = EmailMessage()

    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver

    msg.set_content(body)

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(sender, password)
        smtp.send_message(msg)

    print("Email sent successfully!")


# -----------------------------
# Main Function
# -----------------------------
def main():
    employee_data = load_employee_data("employees.csv")

    report = generate_employee_report(employee_data)

    save_report(report)

    email_body = generate_email(report)

    print(email_body)

    # send_email(
    #     subject="Employee Analytics Report",
    #     body=email_body
    # )


if __name__ == "__main__":
    main()