import os
import shutil

FILES_DIR = "uploaded_files"

def list_files():
    files = []
    if not os.path.exists(FILES_DIR):
        os.makedirs(FILES_DIR)
    for idx, filename in enumerate(os.listdir(FILES_DIR), start=1):
        files.append({"id": idx, "name": filename})
    return files

def delete_file(file_id):
    files = list_files()
    for file in files:
        if str(file["id"]) == str(file_id):
            os.remove(os.path.join(FILES_DIR, file["name"]))
            break

def save_file(file, filename):
    if not os.path.exists(FILES_DIR):
        os.makedirs(FILES_DIR)
    file_path = os.path.join(FILES_DIR, filename)
    file.download(destination_file=file_path)
    return file_path
