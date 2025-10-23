f = open("C:/Users/万向阳/Desktop/read_file.txt",encoding="utf-8")
print(f.readline())
print(f.readlines())
for line in f:
    print(line)
f.close()
# with open("C:/Users/万向阳/Desktop/reag_file.txt",encoding="utf-8") as f:
#     print(f.read())
with open(".\date.txt","r+",encoding="utf-8") as f:
    l = f.readlines()
    for a in l:
        print(a)
    f.write("\noppppppps!")