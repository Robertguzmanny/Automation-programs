import os
import glob

# Specify the folder where ZIP files are located
folder_path = os.path.expanduser("~/Downloads")

# Create a pattern to match all ZIP files
zip_pattern = os.path.join(folder_path, "*.zip")

# Find all ZIP files in the folder
zip_files = glob.glob(zip_pattern)

# Loop through the list of ZIP files and delete them
for zip_file in zip_files:
    os.remove(zip_file)
    print(f"Deleted ZIP file: {zip_file}")

print("All ZIP files have been deleted.")