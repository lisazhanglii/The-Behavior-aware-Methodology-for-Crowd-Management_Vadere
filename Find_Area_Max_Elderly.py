import  json
elderly_number = [0,0,0,0]
with open('pedestrian.json', encoding='utf-8') as a:
    data = json.load(a)
    x = data['dynamicElements']
    for y in range(0,len(x)):
        if  data['dynamicElements'][int(y)]['freeFlowSpeed'] < 0.9:
            m = data['dynamicElements'][int(y)]['position']['x']
            n = data['dynamicElements'][int(y)]['position']['y']
            if m < 50 and 50 <= n:
                elderly_number[0]= elderly_number[0]+1
            if m <50 and n<50:
                elderly_number[3] = elderly_number[3] + 1
            if m >= 50 and n >= 50:
                elderly_number[1] = elderly_number[1] + 1
            if m >= 50 and n < 50:
                elderly_number[2] = elderly_number[2] + 1
    max_value = max(elderly_number)
    max_index = elderly_number.index(max_value)
    target  = max_index+1
    print(target)


