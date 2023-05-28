import json
import random

with open('pedestrian.json', encoding='utf-8') as a:
    data = json.load(a)
    x = data['dynamicElements']
    for y in range(0,len(x)):
        id = data['dynamicElements'][int(y)]['attributes']['id']
        m=data['dynamicElements'][int(y)]['position']['x']
        n=data['dynamicElements'][int(y)]['position']['y']
        # data['dynamicElements'][int(y)]['targetIds'][0]

        if(m>50.0 and n<50.0):
            data['dynamicElements'][int(y)]['targetIds'][0] = 3
        elif(m>50.0 and n>50.0):
            data['dynamicElements'][int(y)]['targetIds'][0] = 2
        elif(m<50.0 and n<50.0):
            data['dynamicElements'][int(y)]['targetIds'][0] = 4
        else:
            data['dynamicElements'][int(y)]['targetIds'][0] = 1


with open('pedestrian.json', 'w') as file:
    json.dump(data, file, indent=2)
    print("Finihsed!")