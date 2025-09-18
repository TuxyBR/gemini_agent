import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types  # type: ignore
from call_functions import available_functions, call_function

load_dotenv()

model = "gemini-2.0-flash-001"
MAX_AGENT_ITERATIONS = 20
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
  verbose = "--verbose" in sys.argv or "-V" in sys.argv
  if verbose:
    print(f"sys args: {sys.argv}")

  args = []
  for arg in sys.argv[1:]:
    if not (arg.startswith("--") or arg.startswith("-")):
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

  final_text = None

  for _ in range(MAX_AGENT_ITERATIONS):
    try:
      response = client.models.generate_content(
        model=model,
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
      )

      if verbose:
        print(
          f"User prompt: {prompt}\n"
          + f"Prompt tokens: {response.usage_metadata.prompt_token_count}\n"
          + f"Response tokens: {response.usage_metadata.candidates_token_count}\n"
        )

      last_added_content = None
      for candidate in response.candidates or []:
        candidate_content = getattr(candidate, "content", None)
        if candidate_content:
          messages.append(candidate_content)
          last_added_content = candidate_content

      last_text_value = None
      if last_added_content and getattr(last_added_content, "parts", None):
        for part in last_added_content.parts or []:
          text_value = getattr(part, "text", None)
          if text_value is not None:
            last_text_value = text_value
            break

      if response.function_calls:
        function_responses = []
        for function_call_part in response.function_calls:
          function_call_result = call_function(function_call_part, verbose)
          if not function_call_result.parts or not function_call_result.parts[0].function_response:
            raise Exception("empty function call result")
          function_responses.append(function_call_result)

        if not function_responses:
          raise Exception("no function responses generated, exiting.")

        messages.extend(function_responses)
        continue

      if last_text_value is not None or (response.text is not None and response.text != ""):
        final_text = response.text if response.text not in (None, "") else last_text_value
        if final_text is not None:
          print(final_text)
        break

      break
    except Exception as exc:
      if verbose:
        print(f"Error while generating content: {exc}")
      break

  else:
    if verbose:
      print("Maximum iterations reached without a final response.")

  return final_text


if __name__ == "__main__":
  main()
