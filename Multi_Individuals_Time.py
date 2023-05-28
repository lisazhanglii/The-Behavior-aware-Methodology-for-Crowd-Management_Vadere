import glob
import os
id_list=[]
selected_id_list=[]
unselected_id_list=[]
individual_end_time = [0.0]*100000
total_time_selected = 0.0
total_time_unselected = 0.0
total_number_selected =0
total_number_unselected =0
max_selected = 0.0
max_unselected=0.0
min_unselected = 1000.0
min_selected = 1000.0
folder_path = "/Users/zhangyixin/CognitionAndBehavior/output"
files_path = os.path.join(folder_path, '*')
files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
folder_path = os.path.join(files[0],'result.txt')
latest_folder =  folder_path#latest file
number_string =input('input the IDs:')
number_string = number_string.replace('[','').replace(']','')
id_list1=number_string.split(',')
for item in id_list1:
    number = int(item)
    id_list.append(number)
print(id_list)

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
            if x in id_list:
                if individual_end_time[x]==0:
                    selected_id_list.append(x)
                    total_number_selected = total_number_selected + 1
                if individual_end_time[x] < float(x1[2]):
                    individual_end_time[x] = float(x1[2])
            else:
                if individual_end_time[x]==0:
                    unselected_id_list.append(x)
                    total_number_unselected = total_number_unselected + 1
                if individual_end_time[x] < float(x1[2]):
                    individual_end_time[x] = float(x1[2])

    for time in selected_id_list:
        if max_selected < individual_end_time[time]:
            max_selected = individual_end_time[time]
            max_selected_id = time
        if min_selected > individual_end_time[time]:
            min_selected = individual_end_time[time]
            min_selected_id = time
        total_time_selected = total_time_selected + individual_end_time[time]
    for time in unselected_id_list:
        if max_unselected < individual_end_time[time]:
            max_unselected = individual_end_time[time]
            max_unselected_id = time
        if min_unselected > individual_end_time[time]:
            min_unselected = individual_end_time[time]
            min_unselected_id = time
        total_time_unselected = total_time_unselected + individual_end_time[time]

    if total_time_selected==0:
        print("the id doesn't exist.")
        exit(0)
    else:
        average_selected = total_time_selected/total_number_selected
        average_unselected=total_time_unselected/total_number_unselected
        print('selected number, average, max, min, max_id, min_id: ')
        print(total_number_selected,average_selected,max_selected,min_selected,max_selected_id,min_selected_id)
        print('unselected number, average, max, min, max_id, min_id: ')
        print(total_number_unselected,average_unselected,max_unselected,min_unselected,max_unselected_id,min_unselected_id)


    print('all average: '+str((total_number_selected*average_selected+total_number_unselected*average_unselected)/(total_number_selected+total_number_unselected)))
    if max_selected>=max_unselected:
        print('all max: '+str(max_selected))
    else:print('all max: '+str(max_unselected))
    if min_selected<=min_unselected:
        print('all min: '+str(min_selected))
    else:print('all min: '+str(min_unselected))

