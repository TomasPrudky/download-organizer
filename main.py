import os
import shutil
from pathlib import Path

file_extensions = {
    "text_files": [
        ".txt", ".md", ".csv", ".log", ".json", ".xml", ".yaml", ".yml"
    ],
    "image_files": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"
    ],
    "audio_files": [
        ".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a", ".wma"
    ],
    "video_files": [
        ".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".mpg"
    ],
    "document_files": [
        ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".odt"
    ],
    "compressed_files": [
        ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"
    ],
    "executable_files": [
        ".exe", ".bat", ".sh", ".bin", ".cmd", ".msi"
    ],
    "code_files": [
        ".py", ".java", ".c", ".cpp", ".cs", ".js", ".html", ".css", ".php", ".rb", ".swift", ".go", ".ts"
    ],
    "other_files":[]
}

def is_known_extension(extension):
    for category, extensions in file_extensions.items():
        if extension.lower() in extensions:
            return True, category
    return False, None

def create_directories(download_path):
    if os.path.exists(download_path):
        for category, extensions in file_extensions.items():
            if extensions:  # Check if the list is not empty
                os.makedirs(os.path.join(download_path, category), exist_ok=True)
        # Create the 'other_files' directory
        os.makedirs(os.path.join(download_path, "other_files"), exist_ok=True)

# Get the path to the user's home directory
home_dir = os.path.expanduser("~")
home_dir_d = "D:/"

# Append the 'Downloads' folder to the home directory path
downloads_folder = os.path.join(home_dir, "Downloads")

# Create the directories if they don't exist
create_directories(downloads_folder)

files = os.listdir(downloads_folder)

for file in files:
    file_path = os.path.join(downloads_folder, file)
    if os.path.isfile(file_path):  # Ensure it is a file
        known, category = is_known_extension(os.path.splitext(file)[1])
        if known:
            target_directory = os.path.join(downloads_folder, category)
        else:
            target_directory = os.path.join(downloads_folder, "other_files")
        
        # Ensure the target directory exists
        os.makedirs(target_directory, exist_ok=True)

        target_path = os.path.join(target_directory, file)
        shutil.move(file_path, target_path)
