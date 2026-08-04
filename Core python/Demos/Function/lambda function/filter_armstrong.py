def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(map(lambda d : int(d)**power,digits))
    return total == n

numbers = list(range(1,1000))
armstrongs = list(filter(is_armstrong,numbers))
print(armstrongs)