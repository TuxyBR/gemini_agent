from google.genai import types  # type: ignore
from config import WORKING_DIR

from functions.get_file_content import *
from functions.get_files_info import *
from functions.run_python import *
from functions.write_file import *

from schemas import *

available_functions = types.Tool(function_declarations=[
  schema_get_files_info,
  schema_get_file_content,
  schema_run_python_file,
  schema_write_file,
])

functions = {
  "get_file_content": get_file_content,
  "get_files_info": get_files_info,
  "run_python_file": run_python_file,
  "write_file": write_file,
}


def call_function(function_call_part, verbose):
  function_name = function_call_part.name
  if verbose:
    print(f"Calling function: {function_name}({function_call_part.args})")
  else:
    print(f" - Calling function: {function_name}")
  try:
    if function_name not in functions:
      return types.Content(
        role="tool",
        parts=[
          types.Part.from_function_response(
            name=function_name,
            response={"error": f"Unknown function: {function_name}"},
          )
        ],
      )

    args = dict(function_call_part.args)
    args["working_directory"] = WORKING_DIR

    function_result = functions[function_name](**args)

    return types.Content(
      role="tool",
      parts=[types.Part.from_function_response(
        name=function_name,
        response={"result": function_result},
      )],
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
