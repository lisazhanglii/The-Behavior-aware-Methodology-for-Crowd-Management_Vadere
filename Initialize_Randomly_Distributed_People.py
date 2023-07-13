import json
import random

random.seed(1)
id_list = []
with open('pedestrian.json', encoding='utf-8') as a:
    data = json.load(a)
    x = data['dynamicElements']
    for y in range(0,len(x)):
        id = data['dynamicElements'][int(y)]['attributes']['id']
        id_list.append(id) #get all the persons' id

number = len(id_list)
import json
import random


def is_in_excluded_area(x, y):

    return (x == 0 or x == 100 or y == 0 or y == 100) or \
        (0 <= x <= 5 and 0 <= y <= 5) or \
        (95 <= x <= 100 and 0 <= y <= 5) or \
        (0 <= x <= 5 and 95 <= y <= 100) or \
        (95 <= x <= 100 and 95 <= y <= 100)


# 加载 JSON 数据
with open('pedestrian.json', encoding='utf-8') as a:
    data = json.load(a)

people = data
tem = data['dynamicElements']
for person in range(0,len(tem)):
    while True:
        x = random.uniform(0.01, 99.9)
        y = random.uniform(0.01, 99.9)


        if is_in_excluded_area(x, y):
            continue


        data['dynamicElements'][int(person)]['position']['x'] = x
        data['dynamicElements'][int(person)]['position']['y'] = y
        break


with open('pedestrian.json', 'w') as file:
    json.dump(data, file, indent=2)
    print("Finihsed randomly distributing the positions of all the persons!")

