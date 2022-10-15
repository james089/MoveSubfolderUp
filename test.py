import os
import shutil

rootdir = 'C:/Users/linbo/PycharmProjects/MoveFolderOut'
for file in os.listdir(rootdir):
    d = os.path.join(rootdir, file)
    if os.path.isdir(d) and 'venv' not in d and '.idea' not in d:
        for subfolderName in os.listdir(d):
            subDir = os.path.join(d,subfolderName)
            print(subDir)
            shutil.move(subDir, rootdir)