# Enumerate Function

l1 = ["Bhindi", "Allo", "Chopsticks", "Chowmein"]

# i = 1
# for item in l1:
#     if i % 2 is not 0:
#         print(f"Jarvis Please buy :- {item}")
#     i += 1

for index, item in enumerate(l1):
    if index % 2 == 0:
        print(f"Jarvis Please buy {item}")
