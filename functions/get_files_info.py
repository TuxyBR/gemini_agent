import os

def get_files_info(working_directory, directory="."):
  full_path = os.path.abspath(os.path.join(working_directory, directory))
  if os.path.isdir(full_path):
    if full_path.startswith(os.path.abspath(working_directory)):
      list_files = ""
      files = os.listdir(full_path)
      for file in files:
        file_path = os.path.join(full_path, file)
        list_files += (f'- {file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}\n')
      return list_files
    return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
  return f'Error: "{directory}" is not a directory'