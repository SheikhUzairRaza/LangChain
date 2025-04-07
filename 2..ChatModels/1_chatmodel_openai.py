from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="GPT-4o", temperature=1.8, max_completion_tokens=50)
result = model.invoke("Hello, Write a fictional story on 'X' at a job interview")
# print(result)
print(result.content)
