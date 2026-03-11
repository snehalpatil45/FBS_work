# accept no of passengers from user and per ticket cost.then accept age of each passenger and then calculate total amount to ticket to travel 
# to travel for all of them based on following condition:
# a.children below 12 = 30 % dicount
# b.senior citizen(above 59) = 50 % discount
# c.others need to pay full

num = int(input('Enter number of passengers :'))
ticket = int(input('Enter ticket cost:'))
total = 0
for i in range(num):
    age = int(input('Enter age:'))
    if(age < 12):
        cost = ticket * 0.7
    elif(age > 59):
        cost = ticket * 0.5
    else:
        cost = ticket
    total = total + cost
print(f'Total amount of ticket is {total}')