#sum of all elements in a list

def sum(num):
    sum = 0
    for num in li:
        sum += num
    return sum

li = [45,18,93,7,1,63]
print(f'Sum:{sum(li)}')