import os
import shutil

folder = "C:/Users/YourName/Desktop/MyFolder"

files = os.listdir(folder)

for f in files:
    
    if f.endswith(".jpg") or f.endswith(".png"):
        os.makedirs(folder + "/Images", exist_ok=True)
        shutil.move(folder + "/" + f, folder + "/Images/" + f)
        
    if f.endswith(".pdf") or f.endswith(".docx") or f.endswith(".txt"):
        os.makedirs(folder + "/Documents", exist_ok=True)
        shutil.move(folder + "/" + f, folder + "/Documents/" + f)
        
    if f.endswith(".mp4") or f.endswith(".avi"):
        os.makedirs(folder + "/Videos", exist_ok=True)
        shutil.move(folder + "/" + f, folder + "/Videos/" + f)

    if f.endswith(".mp3") or f.endswith(".wav"):
        os.makedirs(folder + "/Audio", exist_ok=True)
        shutil.move(folder + "/" + f, folder + "/Audio/" + f)

    if f.endswith(".zip") or f.endswith(".rar"):
        os.makedirs(folder + "/Zipped Files", exist_ok=True)
        shutil.move(folder + "/" + f, folder + "/Zipped Files/" + f)