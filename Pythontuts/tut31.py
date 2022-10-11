# Using With Block To Open Python Files
with open("ankur2.txt") as f:
    a = f.readlines()
    print(a)
f = open("ankur2.txt", "rt")
print(f.readline())
f.close()
