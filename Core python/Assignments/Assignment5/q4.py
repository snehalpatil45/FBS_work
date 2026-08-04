# write a program to print armstrong number within a given range.

start = int(input('Enter start number:'))
end = int(input('Enter end number:'))
for num in range(start,end+1):
    sum = 0
    count = len(str(num))
    for digit in str(num):
        sum = sum + int(digit)**count
    if(sum == num):
        print(f'{num} is a armstrong number')