import os
import shutil

# The folders where files will go
folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Docs": [".html", ".txt", ".pdf", ".css"]
}

# 1. Ensure folders exist (even if you made them, this prevents errors)
for folder_name in folders:
    os.makedirs(folder_name, exist_ok=True)

# 2. Get all files in the current directory
all_files = os.listdir('.')

print("--- STARTING CLEANUP ---")

for file in all_files:
    # Skip this script itself so we don't move it!
    if file == "cleaner.py" or file == "exam_timer.py":
        continue

    # 3. Check file extension and move it
    file_name, file_extension = os.path.splitext(file)
    
    for folder_name, extensions in folders.items():
        if file_extension.lower() in extensions:
            # Construct the move path
            src = file
            dst = f"{folder_name}/{file}"
            
            # Move the file
            shutil.move(src, dst)
            print(f"Moved: {file}  -->  {folder_name}")

print("--- CLEANUP COMPLETE ---")