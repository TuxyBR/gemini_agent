import os

def write_file(working_directory, file_path, content):
  full_path = os.path.abspath(os.path.join(working_directory, file_path))
  abs_working_directory = os.path.abspath(working_directory)
  if full_path.startswith(abs_working_directory):
    try:
      if not os.path.exists(abs_working_directory):
        os.makedirs(abs_working_directory)
      with open(full_path, "w") as f:
        f.write(content)
      return f'Successfully wrote to "{file_path}" ({len(content)} characters written)' 
    except Exception as e:
      return f'Error reading file "{full_path}": {e}'
  return f'Error: Cannot read "{full_path}" as it is outside the permitted working directory ({abs_working_directory})'