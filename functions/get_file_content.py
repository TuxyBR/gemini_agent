import os
from config import MAX_CHARACTERS

def get_file_content(working_directory, file_path):
  full_path = os.path.abspath(os.path.join(working_directory, file_path))
  if os.path.isfile(full_path):
    if full_path.startswith(os.path.abspath(working_directory)):
      try:
        with open(full_path, "r") as f:
          file_content_string = f.read(MAX_CHARACTERS) + (f'\n[...File "{file_path}" truncated at 10000 characters]' if os.path.getsize(full_path) > MAX_CHARACTERS else '')
          return file_content_string
      except Exception as e:
        return f'Error reading file "{file_path}": {e}'
    return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
  return f'Error: File not found or is not a regular file: "{file_path}"'