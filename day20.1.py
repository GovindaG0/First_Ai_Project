from pypdf import PdfReader
from google import genai
from dotenv import load_dotenv
from google.genai import types
import os

load_dotenv()

reader = PdfReader("Loan+Approval+Requirement+Doc.pdf")

text = ""

for page in reader.pages:
    text += page.extract_text()

text = text.replace("\n", " ")
text = text.strip()

prompt = f"""
You are an expert document analyst.

Summarize the following PDF.

Include:

- Purpose
- Main Points
- Important Facts
- Conclusion

Document:

{text}
"""
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

# print(response.text)

question = input("Ask about the PDF: ")

prompt = f"""
Document:

{text}

Question:

{question}

Answer only using the information from the document.
If the answer is not present, say:
"I couldn't find that information in the document."
provide answer in jason format
answer =jason result ,only provide the answer of question not all meta data
"""
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)
print(response.text)