import os

def write_file(working_directory, file_path, content):
  full_path = os.path.abspath(os.path.join(working_directory, file_path))
  if full_path.startswith(os.path.abspath(working_directory)):
    try:
      if not os.path.exists(working_directory):
        os.makedirs(working_directory)
      with open(full_path, "w") as f:
        f.write(content)
      return f'Successfully wrote to "{file_path}" ({len(content)} characters written)' 
    except Exception as e:
      return f'Error reading file "{file_path}": {e}'
  return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'