import json
import random

random.seed(1)
counter = [0, 0, 0, 0]
id_list = []
with open('pedestrian.json', encoding='utf-8') as a:
    data = json.load(a)
    x = data['dynamicElements']
    for y in range(0,len(x)):
        id = data['dynamicElements'][int(y)]['attributes']['id']
        id_list.append(id) #get all the persons' id

number = len(id_list)

with open('pedestrian.json', encoding='utf-8') as a:
    data = json.load(a)
    x = data['dynamicElements']
    for y in range(0,len(x)):
            target = random.randint(1, 4)
            counter[target - 1] += 1
            data['dynamicElements'][int(y)]['targetIds'][0]= random.randint(1, 4)

with open('pedestrian.json', 'w') as file:
    json.dump(data, file, indent=2)
    print("Finihsed randomly distributing the targets of all the persons!")

for i in range(4):
    print("target", i+1, "appears", counter[i],"times")