def merge(listA, listB):
    newlist = list()
    a = 0
    b = 0
    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            newlist.append(listA[a])
            a += 1
        else:
            newlist.append(listB[b])
            b += 1
    while a < len(listA):
        newlist.append(listA[a])
        a += 1
    while b < len(listB):
        newlist.append(listB[b])
        b += 1
    return newlist

def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    else:
        mid = len(input_list) // 2
        left = merge_sort(input_list[:mid])
        right = merge_sort(input_list[mid:])
        newlist = merge(left, right)
        return newlist

a = [10, 43, 23, 77, 44, 234, 1, 5, 99, 1000]
print(merge_sort(a))