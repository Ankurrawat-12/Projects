# Seek(), tell() & More On Python Files

f = open("ankur2.txt")
print(f.tell())
print(f.readline())
f.seek(0)
print(f.tell())
print(f.readline())
f.seek(20)
print(f.tell())
print(f.readline())
f.close()
