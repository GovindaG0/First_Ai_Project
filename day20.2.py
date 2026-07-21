from pypdf import PdfReader
from google import genai
from dotenv import load_dotenv
from google.genai import types
import os

reader=PdfReader("resume.pdf")
text=""
for page in reader.pages:
    text+=page.extract_text()

text=text.replace("\n"," ")
text=text.strip()
# print(text)

prompt='''# Resume Analysis Prompt

You are an expert HR recruiter, technical interviewer, and resume reviewer with experience screening resumes for top technology companies.

Analyze the provided resume thoroughly and extract the requested information accurately. Base your response only on the information explicitly available in the resume. Do not assume or invent details.

## Extract the following information:

1. Full Name
2. Professional Summary (if available)
3. Skills

   * Technical Skills
   * Soft Skills
   * Tools & Technologies
4. Work Experience

   * Company Name
   * Job Title
   * Duration
   * Key Responsibilities
5. Education

   * Degree
   * Institution
   * Graduation Year (if available)
   * CGPA/Percentage (if available)
6. Certifications (if available)
7. Projects (if available)

   * Project Name
   * Technologies Used
   * Brief Description
8. Strengths
9. Weaknesses or Missing Information
10. Suggested Improvements to make the resume more attractive for recruiters
11. Overall Resume Score (0–100)
12. Suitable Job Roles based on the resume

## Response Requirements

* Return the response as valid JSON only.
* Do not include Markdown or code fences.
* If any field is unavailable, return null or an empty array.
* Keep the response concise, professional, and recruiter-friendly.

### Expected JSON Format

{
"name": "",
"professional_summary": "",
"skills": {
"technical": [],
"soft": [],
"tools": []
},
"experience": [
{
"company": "",
"job_title": "",
"duration": "",
"responsibilities": []
}
],
"education": [
{
"degree": "",
"institution": "",
"graduation_year": "",
"cgpa": ""
}
],
"certifications": [],
"projects": [
{
"name": "",
"technologies": [],
"description": ""
}
],
"strengths": [],
"weaknesses": [],
"suggested_improvements": [],
"resume_score": 0,
"recommended_roles": []
}

'''
load_dotenv()
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
respons=client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[prompt,text],
    config=types.GenerateContentConfig(
    response_mime_type="application/json"
)
)

with open("resume.txt","w",encoding="utf-8")as file:
    file.write(respons.text)

# print(respons.text)
