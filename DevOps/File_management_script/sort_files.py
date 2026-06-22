import os
import shutil

# Folder to organize
source_folder = "downloads"

# File extensions and their target folders
file_types = {
    ".pdf": "PDFs",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".docx": "Word",
    ".doc": "Word",
    ".xlsx": "Excel",
    ".xls": "Excel",
    ".txt": "TextFiles"
}

# Create destination folders
for folder in set(file_types.values()):
    os.makedirs(os.path.join(source_folder, folder), exist_ok=True)

# Organize files
for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    # Skip folders
    if not os.path.isfile(file_path):
        continue

    extension = os.path.splitext(file)[1].lower()

    if extension in file_types:
        destination_folder = os.path.join(
            source_folder,
            file_types[extension]
        )

        shutil.move(
            file_path,
            os.path.join(destination_folder, file)
        )

        print(f"Moved: {file} -> {file_types[extension]}")

print("\nFile organization completed!")