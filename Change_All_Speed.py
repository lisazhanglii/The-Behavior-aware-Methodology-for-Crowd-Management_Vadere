import json
import random

number_string =input('input the min speed:')
n = float(number_string)
number_string =input('input the max speed:')
m = float(number_string)

with open('pedestrian.json', encoding='utf-8') as a:
    data = json.load(a)
    x = data['dynamicElements']
    for y in range(0,len(x)):
        data['dynamicElements'][int(y)]['freeFlowSpeed']=random.uniform(n,m)

with open('pedestrian.json', 'w') as file:
    json.dump(data, file, indent=2)
    print("Finihsed!")

