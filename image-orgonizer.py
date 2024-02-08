import os
import shutil
from datetime import datetime

# Define the path to your desktop (adjust as necessary)
desktop_path = os.path.expanduser("~/Desktop")

# Define the destination folder for organized images and screenshots
destination_folder = os.path.join(desktop_path, "Images_and_Screenshots")

# Ensure the destination folder exists
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Define image and screenshot file extensions
image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.heic']  # Add or remove extensions as needed

# Loop through all files on the desktop
for file_name in os.listdir(desktop_path):
    if file_name.lower().endswith(tuple(image_extensions)):
        file_path = os.path.join(desktop_path, file_name)

        # Get the modification time and convert it to a date format (YYYY-MM-DD)
        mod_time = os.path.getmtime(file_path)
        date_folder_name = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d')

        # Create a destination path for this date
        date_folder_path = os.path.join(destination_folder, date_folder_name)
        if not os.path.exists(date_folder_path):
            os.makedirs(date_folder_path)

        # Move the file into the appropriate date folder
        shutil.move(file_path, date_folder_path)
        print(f"Moved '{file_name}' to '{date_folder_path}'.")

print("All images and screenshots have been organized by date.")
