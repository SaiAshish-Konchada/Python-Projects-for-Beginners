# Mode
list1 = [32, 1, 22, 44, 66, 18, 25, 29, 25, 99]
frequency = {}
for i in list1:
    frequency.setdefault(i, 0)
    frequency[i] += 1

frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i
print(mode)
