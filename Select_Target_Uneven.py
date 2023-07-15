import json
import random

# 设置随机种子
random.seed(1)


def is_in_left_top_center(x, y):
    """检查坐标是否在左上角四分之一区的中心的30*30矩阵内"""
    return 45 <= x <= 50 and 50 <= y <= 55


def is_in_left_top_quarter(x, y):
    """检查坐标是否在左上角四分之一区内"""
    return 0.001 <= x <= 49.999 and 50.001 <= y <= 99.999


# 加载 JSON 数据
with open('pedestrian.json', encoding='utf-8') as a:
    data = json.load(a)

# 遍历所有人
for person in data['dynamicElements']:
    x = person['position']['x']
    y = person['position']['y']

    if is_in_left_top_center(x, y):
        # 如果在左上角四分之一区的中心的30*30矩阵内，目标设为 3
        target = 3
    elif is_in_left_top_quarter(x, y):
        # 如果在左上角四分之一区内但不在中心的30*30矩阵内，目标设为 1
        target = 1
    elif x <= 50:
        # 如果在左下角四分之一区内，目标设为 4
        target = 4
    elif y >= 50:
        # 如果在右上角四分之一区内，目标设为 2
        target = 2
    else:
        # 如果在右下角四分之一区内，目标设为 3
        target = 3

    # 更新目标
    person['targetIds'][0] = target

# 保存 JSON 数据
with open('pedestrian.json', 'w') as file:
    json.dump(data, file, indent=2)

print("Finished updating the targets of all persons!")
