# Median
list1 = [32, 1, 22, 44, 66, 18, 25, 29, 25, 99]
list1.sort()

if len(list1) % 2 == 0:
    m1 = list1[len(list1) // 2]
    m2 = list1[len(list1) // 2 - 1]
    median = (m1 + m2) / 2
else:
    median = list1[len(list1) // 2]
print(median)
