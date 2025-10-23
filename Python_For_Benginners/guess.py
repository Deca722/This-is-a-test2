import random
num = random.randint(1, 100)
guess = -1
count = 0
print(" 猜数字游戏（1-100）：最多猜10次哦！")

while guess != num and count < 10:
    try:
        guess = int(input("请输入猜测的数字："))
        count += 1
        if guess > num:
            print(f"大了！还剩{10-count}次机会")
        elif guess < num:
            print(f"小了！还剩{10-count}次机会")
    except ValueError:
        print("输入错误！请填数字～")

if guess == num:
    print(f" 恭喜猜对！共猜了{count}次")
else:
    print(f" 机会用完啦～正确答案是{num}")