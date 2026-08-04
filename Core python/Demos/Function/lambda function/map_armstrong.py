def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(map(lambda d : int(d)**power,digits))
    return total == n

numbers = list(range(1,1000))
flags = list(map(is_armstrong,numbers))
armstrongs = [ n for n,f in zip(numbers,flags)if f]
print(armstrongs)