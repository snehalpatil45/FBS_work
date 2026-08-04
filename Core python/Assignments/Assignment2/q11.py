# wap to accept an integer amount from user and tell minimum number of notes needed for 
# representing the amount

amount = int(input("Enter amount:"))
n500 = amount // 500
amount = amount % 500
n200 = amount // 200
amount = amount % 200
n100 = amount // 100
amount = amount % 100
n50 = amount // 50
amount = amount % 50
n10 = amount // 10
print("500:",n500)
print("200:",n200)
print("100:",n100)
print("50:",n50)
print("10:",n10)