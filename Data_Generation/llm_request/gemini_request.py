import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_gemini = os.environ.get('GEMNI_API_KEY')

if not api_gemini:
    raise ValueError("GEMNI_API_KEY not found in environment variables")

# print(api_gemini)

def test_get_gemini_response():
    api_key = api_gemini
    prompt = "Explain the significance of the Turing Test in artificial intelligence."
    
    result = get_gemini_response(prompt, api_key)
    print(result)

def get_gemini_response(prompt, api_key,model_name="gemini-1.5-flash"):
    # Configure the API key
    genai.configure(api_key=api_key)

    # Initialize the model with default generation settings
    model = genai.GenerativeModel(model_name=model_name)
    print("RESPONSE FROM GEMINI")
    # Start a chat session
    chat_session = model.start_chat()

    # Send the prompt to the model
    response = chat_session.send_message(prompt)

    # Return the model's response text
    return response.text

if __name__ == "__main__":
    test_get_gemini_response()