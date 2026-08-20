roll_str = str(1024170030)
L = [int(digit)*10 for digit in roll_str]

# i)
print(L)

# ii)
L.append(101)
print(L)
L.insert(10, 102)
print(L)
# append() adds element to the last of list, while in insert(index, element) adds element to that specific index in the list

# iii)
L.remove(101)
print(L)
L.pop()
print(L)

# iv)
L.sort()
print(L)
L.sort(reverse=True)
print(L)

# v)
print(L[:3])
print(L[-3:])

# vi)
avg = sum(L)/len(L)
L2 = [x for x in L if x > avg]
print(L2)