import glob
import os

with open('folder_path', 'r') as f:
    folder_path = f.read().strip()
files_path = os.path.join(folder_path, '*')
a = [0.0] * 100
b = []
files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
folder_path = os.path.join(files[0],'result2.txt')
latest_folder =  folder_path#latest file
print("The file name is ")
print(latest_folder)
with open(latest_folder, 'r') as f:
    lines = f.read().splitlines()
    index = 1
    for line in lines:
        if(index!=1):
            target= int(line.split()[-1])
            time = float(line.split()[1])
            if a[target]<time:
                a[target] = time
        index =index+1
    for y in range(0, 10):
        if (a[y]>0.0):
            print("target "+str(y)+" time is "+str(a[y]))






