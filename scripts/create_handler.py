import os
import sys
from pathlib import Path

TEMPLATE = """from aiogram import types
from aiogram.fsm.context import FSMContext

async def {handler_name}({event_arg}: types.{event_type}, state: FSMContext):
    \"\"\"Handle {event_type}\"\"\"
    # Your logic here
    pass
"""

def create_handler(handler_type, folder_path, filename):
    """
    Create a handler file.

    Args:
        handler_type (str): Type of the handler (e.g., message or callback).
        folder_path (str): Path to the folder where the file should be created.
        filename (str): Name of the file and handler function.

    Returns:
        str: Path to the created handler file.
    """
    # Determine event type
    event_type = {
        "message": "Message",
        "callback": "CallbackQuery",
    }.get(handler_type.lower())

    event_arg = {
        "message": "m",
        "callback": "c",
    }.get(handler_type.lower())

    if not event_type or not event_arg:
        raise ValueError("Invalid handler type. Use 'message' or 'callback'.")

    # Prepare paths and names
    handler_name = f"handle_{filename.lower()}"
    folder = Path(folder_path)
    folder.mkdir(parents=True, exist_ok=True)

    # Create file path
    file_path = folder / f"{filename}.py"

    # Write template to file
    with file_path.open("w") as f:
        f.write(TEMPLATE.format(handler_name=handler_name, event_type=event_type, event_arg=event_arg))

    return str(file_path)

if __name__ == "__main__":
    # Ensure correct usage
    if len(sys.argv) != 4:
        print("Usage: python create_handler.py <handler_type> <folder_path> <filename>")
        sys.exit(1)

    handler_type, folder_path, filename = sys.argv[1:]
    try:
        file_path = create_handler(handler_type, folder_path, filename)
        print(f"Handler created at: {file_path}")
    except Exception as e:
        print(f"Error: {e}")
