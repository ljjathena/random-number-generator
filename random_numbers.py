import random

# 获取用户输入的 X 和 Y
X = int(input("请输入一个自然数X，作为随机数的最大范围："))
Y = int(input("请输入要生成的随机数个数Y："))

# 检查 Y 是否大于 X，如果是，无法生成不重复的数
if Y > X:
    print("错误：生成的随机数个数不能超过范围最大值X。")
else:
    # 生成 Y 个 1 到 X 之间的、不重复的随机数
    random_numbers = random.sample(range(1, X + 1), Y)

    # 输出生成的随机数
    print(f"生成的 {Y} 个 1 到 {X} 之间的不重复随机数是：")
    print(random_numbers)
