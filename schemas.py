from google.genai import types  # type: ignore

schema_get_files_info = types.FunctionDeclaration(
  name="get_files_info",
  description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
  parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
      "directory":
      types.Schema(
        type=types.Type.STRING,
        description=
        "The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
      ),
    },
  ),
)

schema_get_file_content = types.FunctionDeclaration(
  name="get_file_content",
  description=
  "Read file contents in the specified file path, constrained to the working directory and a maximum of 10000 characters.",
  parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
      "file_path":
      types.Schema(
        type=types.Type.STRING,
        description=
        "The path to read from a file, relative to the working directory. If not provided, returns an error.",
      ),
    },
    required=["file_path"],
  ),
)

schema_run_python_file = types.FunctionDeclaration(
  name="run_python_file",
  description=
  "Execute Python files in the specified file path with optional arguments, constrained to the working directory.",
  parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
      "file_path":
      types.Schema(
        type=types.Type.STRING,
        description=
        "The path to execute the python file from, must include '.py', relative to the working directory. If not provided, returns an error.",
      ),
      "args":
      types.Schema(
        type=types.Type.ARRAY,
        items=types.Schema(
          type=types.Type.STRING, description=
          "Optional list of arguments to run the python file with. If not provided, runs the file without arguments."),
        description=
        "Optional list of arguments to run the python file with. If not provided, runs the file without arguments.",
      ),
    },
    required=["file_path"],
  ),
)

schema_write_file = types.FunctionDeclaration(
  name="write_file",
  description="Write or overwrite files in the specified file path, constrained to the working directory.",
  parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
      "file_path":
      types.Schema(
        type=types.Type.STRING,
        description=
        "The path, including file name and extension, to write or overwrite, relative to the working directory. If not provided, returns an error.",
      ),
      "content":
      types.Schema(
        type=types.Type.STRING,
        description="The content to add into the created file. If not provided, returns an error.",
      ),
    },
  ),
)
