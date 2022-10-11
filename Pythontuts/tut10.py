# Dictionary & Its Functions Explained
# Dictionary is nothing but key value pairs
t1 = ()
print(type(t1))
l1 = []
print(type(l1))
d1 = {}
print(type(d1))
d2 = {"Shubham": "Burger", "Rohan": "Fish", "Karan": "Rice",
      "Ankur": {"Breakfast": "Maggi", "Lunch": "Fish",
                "Dinner": "Chicken"}}
# d2["Ankit"] = "Junk food"
# d2[420] = "Peach"
# print(d2)
# del d2[420]
# print(d2)
# print(d2["Shubham"])
# print(d2["Ankur"])
# print(d2["Ankur"]["Dinner"])

# d3 = d2  # also affect d2
# del d3["Shubham"]
# d3 = d2.copy()
# del d3["Shubham"]
# print(d2)

# print(d2.get("Ankur"))
d2.update({"Pratishta": "Lollipop"})
print(d2)
print(d2.keys())
print(d2.items() )
