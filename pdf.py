import os
import shutil

download_folder = os.path.expanduser("~/Downloads")
pdf_folder = os.path.expanduser("~/Downloads/Pdf_Folder")  # Renamed for clarity

# Ensure the PDF folder exists
if not os.path.exists(pdf_folder):
    os.makedirs(pdf_folder)

# Loop through all files in the download folder
for file_name in os.listdir(download_folder):
    # Check if the file is a PDF
    if file_name.lower().endswith(".pdf"):
        file_path = os.path.join(download_folder, file_name)
        target_path = os.path.join(pdf_folder, file_name)

        # Move the new PDF to the PDF folder
        shutil.move(file_path, pdf_folder)
        print(f"'{file_name}' has been moved to '{pdf_folder}'.")

print("All PDF files have been moved to the Pdf_Folder.")
