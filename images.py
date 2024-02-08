import os
import shutil

download_folder = os.path.expanduser("~/Downloads")
images_folder = os.path.expanduser("~/Downloads/images")

# Ensure the images folder exists
if not os.path.exists(images_folder):
    os.makedirs(images_folder)
    print(f"Created folder: {images_folder}")

# Loop through all files in the download folder
for file_name in os.listdir(download_folder):
    # Check if the file is an image
    if file_name.lower().endswith((".heic", ".png", ".jpg", ".jpeg")):
        file_path = os.path.join(download_folder, file_name)
        target_path = os.path.join(images_folder, file_name)

        # If the image already exists in the images folder, remove it
        if os.path.exists(target_path):
            os.remove(target_path)
            print(f"Removed existing file: {target_path}")

        # Move the new image to the images folder
        shutil.move(file_path, images_folder)
        print(f"Moved '{file_name}' to '{images_folder}'.")

print("All eligible image files have been processed.")
