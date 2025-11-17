import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from pprint import pprint

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():
    verbose = False

    if len(sys.argv) < 2:
        print("Usage: python main.py <your_input> [-v|--verbose]")
        sys.exit(1)

    if "-v" in sys.argv or "--verbose" in sys.argv:
        verbose = True
    
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    user_prompt = " ".join(args)  

    if verbose:
        print("[DEBUG] User input:", user_prompt)

    messages = [
        types.Content(
            role="user", 
            parts=[types.Part(text=user_prompt)]
            ),
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )

    if verbose:
        print("[DEBUG] Raw response object:")
        pprint(response.model_dump())
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    else:
        print(response.text)

if __name__ == "__main__":
    main()