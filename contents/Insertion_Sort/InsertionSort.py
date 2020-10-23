import random
array = []
for i in range(10):
    array.append(random.randint(1, 10))
# creates array ----------------------->

key = 0
for i in range(len(array)):
    key = i
    for j in range(i, 0, -1):
        if(array[key] < array[j]):
            z = array[j]
            array[j] = array[key]
            array[key] = z
            key = j
