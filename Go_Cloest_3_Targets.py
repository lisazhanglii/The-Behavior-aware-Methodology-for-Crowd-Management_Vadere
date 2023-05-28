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
        if id in elderly_list:
            data['dynamicElements'][int(y)]['targetIds'][0] = 1
        else:
            distance_2 = numpy.square(m-97.5) + numpy.square(n-97.5)
            distance_3 = numpy.square(m-97.5) + numpy.square(n-2.5)
            distance_4 = numpy.square(m-2.5) + numpy.square(n-2.5)
            a = distance_2
            b = distance_3
            c = distance_4
            min_distance = min(a, b, c)

            if min_distance == distance_2:
                target = 2
            elif min_distance == distance_3:
                target = 3
            else:
                target = 4

            data['dynamicElements'][int(y)]['targetIds'][0] = target

# Save the modified pedestrian.json
with open('pedestrian.json', 'w') as file:
    json.dump(data, file, indent=2)

print("Finished!")
