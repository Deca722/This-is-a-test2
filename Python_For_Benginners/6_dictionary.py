phone_number = {
    ("mike",12):"110",
    ("mike",21):"120",
    "jhon":"119"
}
print(phone_number[("mike",12)])
print(phone_number[("mike",21)])
phone_number["baby"] = "911"
print(("mike",12) in phone_number)
print("mike" in phone_number)
del phone_number["jhon"]
print(len(phone_number))
total = 0
for i in range(1,101):
    total = i + total
    print(total)

list1=["你","好","吗","兄","弟"]
for char in list1:
    print(char)

for i in range(len(list1)):
    print(list1[i])

i = 0
while i < len(list1):
    print(list1[i])
    i = i + 1
# 使用大括号 {} 来创建空字典
emptyDict = {}

# 打印字典
print(emptyDict)

# 查看字典的数量
print("Length:", len(emptyDict))

# 查看类型
print(type(emptyDict))