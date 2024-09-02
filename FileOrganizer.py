import os
import shutil

path = input("Enter path: ")
file = os.listdir(path)

if "videos" not in file:
    os.makedirs(path+"/videos")
if "songs" not in file:
    os.makedirs(path+"/songs")
if "images" not in file:
    os.makedirs(path+"/images")
if "pdf" not in file:
    os.makedirs(path+"/pdf")

for i in file:
    if ".mp4" in i or ".mov" in i or "mkv" in i:
        shutil.move(path+'/'+i, path+'/videos')
    elif ".mp3" in i:
        shutil.move(path+'/'+i, path+'/songs')
    elif ".png" in i or 'jpg' in i or 'jpge' in i:
        shutil.move(path+'/'+i, path+'/images')
    elif '.pdf' in i:
        shutil.move(path+'/'+i, path+'/pdf')
