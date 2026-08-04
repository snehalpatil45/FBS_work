# find maximum and minimum

def find_max_min(num):
    max_val = num[0]
    min_val = num[0]
    for num in li:
        if(num > max_val):
            max_val = num
        if(num < min_val):
            min_val = num
    return max_val,min_val

li = [45,18,93,7,1,63]
max , min = find_max_min(li)
print(f'Max:{max},Min:{min}')