import json
import numpy

# Load selected.json and get the elderly list
with open('selected.json', 'r', encoding='utf-8') as f:
    elderly_list = json.load(f)

# number of elderly
number = len(elderly_list)

# Load pedestrian.json
with open('pedestrian.json', encoding='utf-8') as a:
    data = json.load(a)
    x = data['dynamicElements']
    for y in range(0, len(x)):
        id = data['dynamicElements'][int(y)]['attributes']['id']
        m = data['dynamicElements'][int(y)]['position']['x']
        n = data['dynamicElements'][int(y)]['position']['y']
        if 20 <= m < 30 and 70 <= n:
            if m+n >= 100:
                data['dynamicElements'][int(y)]['targetIds'][0] = 2
            else:
                data['dynamicElements'][int(y)]['targetIds'][0] = 4
        if 20 <=m <30 and n<70:
            data['dynamicElements'][int(y)]['targetIds'][0] = 4
        if m>=30 and n>=70:
            data['dynamicElements'][int(y)]['targetIds'][0] = 2
        if m>=30 and n<70:
            data['dynamicElements'][int(y)]['targetIds'][0] = 3
        if id in elderly_list:
            data['dynamicElements'][int(y)]['targetIds'][0] = 1

# Save the modified pedestrian.json
with open('pedestrian.json', 'w') as file:
    json.dump(data, file, indent=2)

print("Finished!")
