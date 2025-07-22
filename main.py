import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types # type: ignore

load_dotenv()

model = "gemini-2.0-flash-001"

def main():
  args = []
  for arg in sys.argv[1:]:
    if not arg.startswith("--"):
      args.append(arg)
  
  if not args:
    print("Usage: python3 main.py <prompt> [--verbose]")
    sys.exit(1)

  api_key = os.environ.get("GEMINI_API_KEY")
  client = genai.Client(api_key=api_key)
  
  prompt = args[0]
  
  messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
  ]
  
  response = client.models.generate_content(
    model=model, contents=messages
  )
  
  print(f"User prompt: {prompt}\nPrompt tokens: {response.usage_metadata.prompt_token_count} \nResponse tokens: {response.usage_metadata.candidates_token_count}")

  print("Answer:")
  print(response.text)

if __name__ == "__main__":
  main()

