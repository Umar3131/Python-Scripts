#____________---File Organization----________________#

import os
import shutil

FILE_CATEGORIES = {
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.csv'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
    'Videos': ['.mp4', '.mkv', '.mov'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.html', '.css'],
}

def organize_files(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
    
        if os.path.isdir(filepath):
            continue

    
        file_ext = os.path.splitext(filename)[1].lower()
        for category, extensions in FILE_CATEGORIES.items():
            if file_ext in extensions:
                target_folder = os.path.join(directory, category)
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)
                shutil.move(filepath, os.path.join(target_folder, filename))
                print(f"Moved {filename} to {category} folder.")
                break

directory = 'C:\\Users\\HP\\Desktop\\File organization example'
organize_files(directory)
