#1.pass: to neglect expected indentation error.
for i in range(1,6):
     pass

# 2.break : to terminate loop.
for i in range(1,6):
     if(i==3):
         break
     print(i)

#3. continue: to stop current iteration.
for i in range(1,6):
     if(i==3):
         continue
     print(i)

# 4. else: this block of code will execute,
# when loop will executed successfully.
for i in range(1,6):
    if(i==4):
        break
    print(i)
else:
    print('else block executed')