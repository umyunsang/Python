list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 7, 8, 9, 10]

same_val = False

for n1 in list1:
    if n1 in list2:
        same_val = True
        break

print(same_val)
