import random

# 石头剪刀布
player = int(input("请输入您要出的拳：1：石头；2：剪刀；3：布\n"))

computer = random.randint(1, 3)

print("玩家出 %d - 电脑出 %d" % (player, computer))

# 比较胜负
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("玩家胜")
elif player == computer:

    print("平局")
else:

    print("电脑胜")
