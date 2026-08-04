def is_prime(n):
    if (n < 2):
        return False
    for i in range(2,int(n**0.5)+1):
        if (n%i == 0):
            return False
    return True

numbers = [2,3,4,5,9,11,13,15,17]
result = list(map(is_prime,numbers))
print(result)