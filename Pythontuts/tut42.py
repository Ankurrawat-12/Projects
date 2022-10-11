# Time Module In Python

import time


# who is faster for loop or while loop
k = 0
initial = time.time()
print(initial)
while k < 100:
    print(k)
    time.sleep(2)
    k += 1
print("While loop run in ", time.time() - initial, " seconds")
print()
initial2 = time.time()
print(initial2)
for i in range(100):
    print(i)
print("For loop run in ", time.time() - initial2, " seconds")


"""
localtime = time.asctime(time.localtime(time.time()))
# localtime = time.asctime()
# localtime = time.localtime()
print(localtime)
"""
