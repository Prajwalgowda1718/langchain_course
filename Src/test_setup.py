import os #importing the OS
from dotenv import load_dotenv #this
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env file
load_dotenv()

# Check if API key is loaded
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ GOOGLE_API_KEY not found. Check your .env file.")
    exit(1)

print("✅ API key loaded successfully") 

# Test a simple LLM call using Gemini
try:
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
    response = llm.invoke("what is capital ity of India")
    print(f"✅ LLM connection successful!")
    print(f"Response: {response.content}") 
except Exception as e:
    print(f"❌ Error: {e}")

finally:
    print("Execution completed")
    
    