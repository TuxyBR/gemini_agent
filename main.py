import os
from dotenv import load_dotenv
from google import genai

model = "gemini-2.0-flash-001"
contents = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model=model, contents=contents
)

def main():
    print("Hello from gemini-agent!")
    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count} \nResponse tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()

