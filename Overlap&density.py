import glob
import os
import json
import pandas as pd
import re
PI = 3.14
def area(ped_area,id):
    with open('pedestrian.json', encoding='utf-8') as a:
        data = json.load(a)
        x = data['measurementAreas']
        for y in range(0, len(x)):
            id_now = int(data['measurementAreas'][int(y)]['id'])
            if id_now == id:
                width = round(data['measurementAreas'][int(y)]['shape']['width'], 2)
                height = round(data['measurementAreas'][int(y)]['shape']['height'], 2)
                # print(height)
                # print(width)
                area = (width) * (height)
                percentage = round(ped_area/area,2)
                print("The max occupied percentage of area "+str(id_now)+": "+str(percentage))
                return float(percentage)
        return 0

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def overlap(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        second_line = lines[1]
        first_number = int(second_line.split()[0])
        return str(first_number)


area_list = []
folder_path = "/Users/zhangyixin/CognitionAndBehavior/output"
files_path = os.path.join(folder_path, '*')
files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
folder_path=files[0]
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        if "overlapCount" in file_path:
            overlapcount= overlap(file_path)
        elif "AreaDensity" in file_path:
            result = re.search("(.*)AreaDensity(.*).txt", file_path)
            if result:
                id = result.group(2)
            # 用pandas读取txt文件，并指定第一行是列名
                df = pd.read_csv(file_path, header=0, delim_whitespace=True)
            # 找到第三列的最大值
                max_num = df.iloc[:, 1].max()
                # print(max_num)
                total_area_ped = max_num*PI*0.2*0.2
                area_list.append(area(total_area_ped,int(id)))
    print("The average max occuioped percentage of areas: " + str(calculate_average(area_list)))
    print("The total overlapping number: " +overlapcount)


# folder_path = os.path.join(files[0],'result.txt')
# print(folder2)
# # files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
# for file in folder2:
#     if file.startswith("AreaDensity"):
#         print(file)
# def pedNumber():
#
#

#
#
# folder_path_area = os.path.join(files[0],'AreaDensity1.txt')
# folder_path = os.path.join(files[0],'EndTime.txt')
# latest_folder =  folder_path_ped#latest file
# with open(latest_folder, 'r') as file:
#     line = file.readline()
#     counts = 1
#     first = 0
#     while line:
#         if counts >= 50000000:
#             break
#         line = file.readline()
#         if line:
#             counts += 1
#     counts = counts-1
#     print(counts)
