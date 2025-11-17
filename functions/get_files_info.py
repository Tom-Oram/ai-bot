import os

def get_files_info(working_directory, directory="."):
    try:
        full_path = os.path.abspath(os.path.join(working_directory, directory))

        working_directory_abs = os.path.abspath(working_directory)

        if not full_path.startswith(working_directory_abs):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'

        output_lines = []

        for item in os.listdir(full_path):
            item_path = os.path.join(full_path, item)

            try:
                is_dir = os.path.isdir(item_path)
                size = os.path.getsize(item_path)
            except Exception as e:
                return f"Error: Failed to access '{item}': {e}"

            output_lines.append(
                f"- {item}: file_size={size} bytes, is_dir={str(is_dir)}"
            )

        return "\n".join(output_lines)

    except Exception as e:
        return f"Error: {e}"