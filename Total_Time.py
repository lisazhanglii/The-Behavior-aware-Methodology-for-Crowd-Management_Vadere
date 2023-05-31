import glob
import os

with open('folder_path', 'r') as f:
    folder_path = f.read().strip()
files_path = os.path.join(folder_path, '*')
files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
folder_path = os.path.join(files[0],'result.txt')
latest_folder =  folder_path#latest file
print("The file name is ")
print(latest_folder)
with open(latest_folder, 'r') as f:
    lines = f.read().splitlines()
    last_line = lines[-1]
    # print (last_line)
    x = last_line.split()
    print("The experiment stops at ")
    print(x[2])
