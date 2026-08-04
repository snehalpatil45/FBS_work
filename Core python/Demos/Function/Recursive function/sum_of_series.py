def sumOfseries(n):
    if(n > 0):
        return n + sumOfseries(n-1)
    elif(n == 0):
        return 0
    else:
        return None
    
n = 5
res = sumOfseries(n)
print(res)