from tabnanny import verbose
from google.genai import types  # type: ignore

from schemas import *

available_functions = types.Tool(
  function_declarations=[
    schema_get_files_info,
    schema_get_file_content,
    schema_run_python_file,
    schema_write_file,
  ]
)


def call_function(function_call_part, verbose=False):
  function_name = function_call_part.name
  if verbose:
    print(f"Calling function: {function_name}({function_call_part.args})")
  else:
    print(f" - Calling function: {function_name}")
  try:
    function_result = function_name('./calculator', **function_call_part.args)
    return types.Content(
      role="tool",
      parts=[
        types.Part.from_function_response(
          name=function_name,
          response={"result": function_result},
        )
      ],
    )
  except Exception as e:
    return types.Content(
      role="tool",
      parts=[
        types.Part.from_function_response(
          name=function_name,
          response={"error": f"Unknown function: {function_name}"},
        )
      ],
    )
