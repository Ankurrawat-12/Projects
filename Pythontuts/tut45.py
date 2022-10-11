# How Import Works In Python?

import tut45import
"""
import sys

# pathlist = sys.path
# print(sys.path)
# print(type(pathlist))
# for items in pathlist:
#     print(items)

print(sys.path)
"""

from sklearn.ensemble import RandomForestClassifier
print(RandomForestClassifier())

# from tut45import import a  # but don't use this if a is also in
# other module or file which you imported like this then if you want
# print a then it will create an ambiguity , so import full module or
# file

print(tut45import.a)

tut45import.printjoke("This is me")
# print(a)
