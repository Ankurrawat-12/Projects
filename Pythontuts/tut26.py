# Open(), Read() & ReadLine() For Reading File

f = open("ankur.txt", "rt")
list1 = f.readlines()
print(list1)
# print(f.readline())
# print(f.readline())
# content = f.read()

# for line in content:
#     print(line)
# for line in f:
#     print(line, end="")
# print(content)
# content = f.read(344)
# print("1", content)
# content = f.read(3)
# print("2", content)
f.close()
