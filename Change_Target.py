import json
import random
id_list = []
number_string =input('intput the id you want to change:')
number_string = number_string.replace('[','').replace(']','')
id_list1=number_string.split(',')
for item in id_list1:
    number = int(item)
    id_list.append(number)
number = len(id_list)
number_string =input('input the new target:')
target = int(number_string)
with open('pedestrian.json', encoding='utf-8') as a:
    data = json.load(a)
    x = data['dynamicElements']
    print(len(x))
    print('changed id are:')
    print(id_list)
    for y in range(0,len(x)):
        if (data['dynamicElements'][int(y)]['attributes']['id'] in id_list):
            data['dynamicElements'][int(y)]['targetIds'][0]= target
with open('pedestrian.json', 'w') as file:
    json.dump(data, file, indent=2)
    print("Finihsed!")