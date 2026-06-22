import os
import shutil

# Source folder to back up
source_folder = r"D:\MY_WORK\DevOps\Automation_script\documents"

# Backup folder (will be created automatically)
backup_folder = r"D:\MY_WORK\DevOps\Automation_script\Backup"

# Create backup folder if it doesn't exist
os.makedirs(backup_folder, exist_ok=True)

# Copy all files
for file in os.listdir(source_folder):
    source_path = os.path.join(source_folder, file)
    destination_path = os.path.join(backup_folder, file)

    if os.path.isfile(source_path):
        shutil.copy2(source_path, destination_path)
        print(f"Copied: {file}")

print("\nBackup completed successfully!")