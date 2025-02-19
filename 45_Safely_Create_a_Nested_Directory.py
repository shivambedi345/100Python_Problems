from pathlib import Path

directory_path = Path("parent_folder/child_folder/grandchild_folder")

try:
    directory_path.mkdir(parents=True, exist_ok=True)
    print(f"Directory created: {directory_path}")
except OSError as e:
    print(f"Error creating directory: {e}")