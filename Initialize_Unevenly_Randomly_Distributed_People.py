import json
import random

# 设置随机种子
random.seed(1)


def is_in_excluded_area(x, y):
    """检查坐标是否在边界或者四个角落的小方框内"""
    return (x == 0 or x == 100 or y == 0 or y == 100) or \
        (0 <= x <= 5 and 0 <= y <= 5) or \
        (95 <= x <= 100 and 0 <= y <= 5) or \
        (0 <= x <= 5 and 95 <= y <= 100) or \
        (95 <= x <= 100 and 95 <= y <= 100)


# 加载 JSON 数据
with open('pedestrian.json', encoding='utf-8') as a:
    data = json.load(a)

people = data['dynamicElements']
for person in people:
    while True:
        # 根据概率选择区域
        region = random.choices(["upper_left", "upper_right", "lower_left", "lower_right"],
                                weights=[0.75, 0.1, 0.1, 0.05], k=1)[0]

        if region == "upper_left":
            x = random.uniform(0.01, 50)  # 考虑到小方框
            y = random.uniform(50.01, 99.99)  # 考虑到小方框
        elif region == "upper_right":
            x = random.uniform(50.01, 99.99)  # 考虑到小方框
            y = random.uniform(50.01, 99.99)  # 考虑到小方框
        elif region == "lower_left":
            x = random.uniform(0.01, 50)  # 考虑到小方框
            y = random.uniform(0.01, 50)  # 考虑到小方框
        else:  # lower_right
            x = random.uniform(50.01, 99.99)  # 考虑到小方框
            y = random.uniform(0.01, 50)  # 考虑到小方框

        if is_in_excluded_area(x, y):
            continue

        # 更新每个人的位置
        person["position"]["x"] = x
        person["position"]["y"] = y

        break  # 成功生成了一个满足条件的坐标，所以可以跳出循环

# 保存回 JSON 文件
with open('pedestrian.json', 'w', encoding='utf-8') as a:
    json.dump(data, a, ensure_ascii=False, indent=2)

print("Finished randomly distributing the positions of all the persons!")
