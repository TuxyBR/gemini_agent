import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types  # type: ignore
from call_functions import available_functions

load_dotenv()

model = "gemini-2.0-flash-001"
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""


def main():
  verbose = "--verbose" in sys.argv  #
  if verbose:
    print(f"sys args: {sys.argv}")  #

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

  generate_prompt(client, prompt, verbose)



def generate_prompt(client, prompt, verbose):
  messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
  ]

  response = client.models.generate_content(
    model=model,
    contents=messages,
    config=types.GenerateContentConfig(
      tools=[available_functions], system_instruction=system_prompt
    ),
  )
  
  if verbose:
    print(
      f"User prompt: {prompt}\nPrompt tokens: {response.usage_metadata.prompt_token_count} \nResponse tokens: {response.usage_metadata.candidates_token_count}"
    )
    
  if not response.function_calls:
    print (response.text)
    return response.text

  for function_call_part in response.function_calls:
    print(f"Calling function: {function_call_part.name}({function_call_part.args})")


if __name__ == "__main__":
  main()
