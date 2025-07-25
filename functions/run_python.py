import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
  full_path = os.path.abspath(os.path.join(working_directory, file_path))
  abs_working_directory = os.path.abspath(working_directory)
  if full_path.startswith(abs_working_directory):
    try:
      if os.path.exists(full_path):
        if file_path.endswith('.py'):
          try:
            output = []
            result = subprocess.run(['uv', 'run', full_path, *args], capture_output=True, text=True, timeout=30)
            
            if result.stdout:
              output.append(f"STDOUT:\n{result.stdout}")
            if result.stderr:
              output.append(f"STDERR:\n{result.stderr}")

            if result.returncode != 0:
              output.append(f"Process exited with code {result.returncode}")

            return "\n".join(output) if output else "No output produced."
          except subprocess.TimeoutExpired:
            return(f'Error: Code Timeout')
        return f'Error: "{file_path}" is not a Python file.'
      return f'Error: File "{file_path}" not found.'
    except Exception as e:
      return f'Error reading file "{full_path}": {e}'
  return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'