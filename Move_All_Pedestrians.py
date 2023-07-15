import json
import random

with open('pedestrian.json', encoding='utf-8') as a:
    data = json.load(a)
    x = data['dynamicElements']
    for y in range(0,len(x)):
        id = data['dynamicElements'][int(y)]['attributes']['id']
        data['dynamicElements'][int(y)]['position']['x']=data['dynamicElements'][int(y)]['position']['x']+20
        data['dynamicElements'][int(y)]['position']['y']  = data['dynamicElements'][int(y)]['position']['y'] -20

with open('pedestrian.json', 'w') as file:
    json.dump(data, file, indent=2)
    print("Finihsed!")