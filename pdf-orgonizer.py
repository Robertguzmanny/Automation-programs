import os
import shutil
from datetime import datetime

# Define the path to your desktop (adjust as necessary)
desktop_path = os.path.expanduser("~/Desktop")

# Define the destination folders for organized documents
pdf_destination_folder = os.path.join(desktop_path, "PDFs_by_Date")

# Ensure the destination folders exist
if not os.path.exists(pdf_destination_folder):
    os.makedirs(pdf_destination_folder)

# Define file extensions for PDFs
pdf_extensions = ['.pdf']  # Only PDF

# Loop through all files on the desktop
for file_name in os.listdir(desktop_path):
    if file_name.lower().endswith(tuple(pdf_extensions)):
        file_path = os.path.join(desktop_path, file_name)

        # Get the modification time and convert it to a date format (YYYY-MM-DD)
        mod_time = os.path.getmtime(file_path)
        date_folder_name = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d')

        # Create a destination path for this date within the PDF folder
        date_folder_path = os.path.join(pdf_destination_folder, date_folder_name)
        if not os.path.exists(date_folder_path):
            os.makedirs(date_folder_path)

        # Move the PDF file into the appropriate date folder
        shutil.move(file_path, date_folder_path)
        print(f"Moved '{file_name}' to '{date_folder_path}'.")

print("All PDF files have been organized by date.")
