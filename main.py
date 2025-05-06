import google.generativeai as genai
from dotenv import load_dotenv
import os
import sys

load_dotenv()

gen_api_key = os.getenv("GEMINI_API_KEY")

if not gen_api_key:
    print("ERROR: API KEY not found in .env file.")
    sys.exit(1)

genai.configure(api_key=gen_api_key)

model = genai.GenerativeModel("gemini-2.0-flash")

chat = model.start_chat()

print("Gemini Terminal chat (Type 'exit' or 'quit' to end.)")

while True:
    user_input = input("You ~ ").strip()

    if user_input.lower() in ["exit","quit"]:
        print("Goodbye!")
        break

    try:
        response = chat.send_message(user_input)
        print("Gemini ~ ", response.text)
    except Exception as e:
        print("Error: ",e)
