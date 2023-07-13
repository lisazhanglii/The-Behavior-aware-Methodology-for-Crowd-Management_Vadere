import json
import random

random.seed(1)
id_list = []
number_string =input('how many people do you want to change:')
number = int(number_string)
number_string =input('input the min speed:')
n = float(number_string)
number_string =input('input the max speed:')
m = float(number_string)
with open('pedestrian.json', encoding='utf-8') as a:
    data = json.load(a)
    x = data['dynamicElements']
    for y in range(0,len(x)):
        id = data['dynamicElements'][int(y)]['attributes']['id']
        id_list.append(id)
    selected = random.sample(id_list, k=number)
    print('changed id are:')
    print(selected)
    with open('selected.json', 'w',encoding="utf-8") as file:
        json.dump(selected, file)
    # for y in range(0,len(x)):
    #     if (data['dynamicElements'][int(y)]['attributes']['id'] in selected):
    #
    #         data['dynamicElements'][int(y)]['freeFlowSpeed']=random.uniform(n,m)

# with open('elderly.json', 'w') as file:
#     json.dump(selected, file)
# with open('pedestrian.json', 'w') as file:
#     json.dump(data, file, indent=2)
#     print("Finihsed!")

