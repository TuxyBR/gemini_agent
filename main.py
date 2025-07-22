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

if __name__ == "__main__":
    main()

