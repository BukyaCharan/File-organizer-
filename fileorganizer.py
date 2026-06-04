import os
import shutil


folder = input("Enter the folder path to organize: ").strip()


if not os.path.exists(folder):
    print("Folder not found!")
else:
    print(f"\nOrganizing: {folder}\n")

    for f in os.listdir(folder):

       
        if os.path.isdir(os.path.join(folder, f)):
            continue

      
        if f.endswith(".jpg") or f.endswith(".jpeg") or f.endswith(".png") or f.endswith(".gif"):
            category = "Images"
        elif f.endswith(".pdf") or f.endswith(".docx") or f.endswith(".txt") or f.endswith(".doc"):
            category = "Documents"
        elif f.endswith(".mp4") or f.endswith(".avi") or f.endswith(".mkv") or f.endswith(".mov"):
            category = "Videos"
        elif f.endswith(".mp3") or f.endswith(".wav") or f.endswith(".aac"):
            category = "Audio"
        elif f.endswith(".zip") or f.endswith(".rar") or f.endswith(".tar"):
            category = "Zipped Files"
        elif f.endswith(".py") or f.endswith(".js") or f.endswith(".html") or f.endswith(".css"):
            category = "Code"
        else:
            category = "Others"

       
        destination = os.path.join(folder, category)
        os.makedirs(destination, exist_ok=True)

        shutil.move(os.path.join(folder, f), os.path.join(destination, f))
        print(f"Moved: {f}  →  {category}/")

    print("\nDone! All files are organized.")
