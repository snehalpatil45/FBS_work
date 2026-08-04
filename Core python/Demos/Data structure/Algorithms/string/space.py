# calculate spaces in given string
str = 'snehal patil'
count = 0
for char in str:
    if char.isspace():
        count += 1
print(count)