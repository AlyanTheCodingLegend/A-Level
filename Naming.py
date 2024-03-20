import os

def rename_photos("C:/main_directory/Train/Bamboo/"):
    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    count = 1
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.ai', '.jpg', '.jpeg')):
            new_name = f"bamboo{count}"
            new_path = os.path.join(folder_path, new_name + os.path.splitext(filename)[1])
            old_path = os.path.join(folder_path, filename)
            os.rename(old_path, new_path)
            count += 1

if  folder_path = input("Enter the folder path: "):
    rename_photos(folder_path)
    print("Photos renamed successfully.")