# F-Strings & String Formatting In Python
import math

me = "Ankur"
no = 12
# a = "this is %s %s"%(me, no)  # can also use %s %i %d %u %e %f %c %ld
# a = "This is {1} {0}"
# b = a.format(me, no)
# print(b)
a = f"This is {me} {no} {math.cos(65)} {math.floor(math.cos(65))} {math.ceil(math.cos(65))}"
print(a)
