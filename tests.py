import subprocess
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

def tests():
  result = run_python_file("calculator", "main.py")
  print(result)

  result = run_python_file("calculator", "main.py", ["3 + 5"])
  print(result)

  result = run_python_file("calculator", "tests.py")
  print(result)

  result = run_python_file("calculator", "../main.py")
  print(result)

  result = run_python_file("calculator", "nonexistent.py")
  print(
    f'STDOUT:\n{result.stdout}' if len(result.stdout) else f'No output produced.' + 
    f'\nSTDERR:{result.stderr}' if len(result.stderr) else '' +
    f'\nProcess exited with code {result.returncode}' if result.returncode else ''
    ) if isinstance(result, subprocess.CompletedProcess) else print (result)

if __name__ == "__main__":
  tests()