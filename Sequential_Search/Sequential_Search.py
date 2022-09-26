def sequential_search(list_, n):
    found = False
    for i in list_:
        if i == n:
            found = True
            break
    return found

numbers = list(range(0, 25))
print(sequential_search(numbers, 23))