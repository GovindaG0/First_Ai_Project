from google import genai
from dotenv import load_dotenv
from google.genai import types
import os

load_dotenv()

client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
def resume_extracter(prompt,resume):
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt + "\n" + resume,
    config=types.GenerateContentConfig(
        response_mime_type="application/json"
    )
   
)
    return response.text

def resumeextraction():
    prompt = """
Act as a professional resume information extractor.

The user will provide resume text.

Your task is to extract the following information:

- email
- phone_number
- skills
- experience
- education

Rules:
1. Return ONLY valid JSON.
2. Do not include any explanation or additional text.
3. If a field is not found, return null.
4. Skills, experience, and education should always be returned as arrays.
5. Preserve the original information as closely as possible.

Expected JSON format:

{
  "email": "example@email.com",
  "phone_number": "9876543210",
  "skills": [
    "Python",
    "Java",
    "SQL"
  ],
  "experience": [
    {
      "company": "ABC Technologies",
      "designation": "Software Engineer",
      "duration": "Jan 2023 - Present"
    }
  ],
  "education": [
    {
      "degree": "Bachelor of Engineering",
      "institution": "XYZ University",
      "year": "2024"
    }
  ]
}

Resume Text:
"""
    return prompt

def resume_text():
    with open("resume.txt","r")as file:
        data=file.read()
        return data
 
def main():
    resume=resume_text()
    prompt=resumeextraction()
    result=resume_extracter(prompt,resume)
    print(result)

main()
    
    
