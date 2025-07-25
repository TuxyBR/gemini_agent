from google.genai import types # type: ignore

from schemas import *

available_functions = types.Tool(
  function_declarations=[
    schema_get_files_info,
    schema_get_file_content,
    schema_run_python_file,
    schema_write_file,
  ]
)