list1 = [1, 2, 3]
list2 = [4, 5, 6]

list3 = []

for i in range(len(list1)):
    sum = list1[i] + list2[i]
    list3.append(sum)
    i += 1

print list3