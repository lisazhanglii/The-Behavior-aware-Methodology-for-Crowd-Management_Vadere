import glob
import os

with open('folder_path', 'r') as f:
    folder_path = f.read().strip()
files_path = os.path.join(folder_path, '*')
files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
folder_path = os.path.join(files[0],'result.txt')
latest_folder =  folder_path#latest file
number_string =input('input the number:')
number = int(number_string)
with open(latest_folder, 'r') as file:
    line = file.readline()
    counts = 1
    first = 0
    endtime=""
    while line:
        if counts >= 50000000:
            break
        line = file.readline()
        if line:
            counts += 1
            x1 = line.split()
            x=int(x1[0])
            if x==number:
                # first += 1
                # if first==1:
                #     starttime = x[]
                endtime = x1[2]

    print(endtime)
