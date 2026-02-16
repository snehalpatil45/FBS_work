#1. and : if both operands are true then return true,
          #otherwise false
print(True and True)
print(True and False)

#2. or : if both operands are false then return false,
         #otherwise true
print(False or False)
print(True or False) 

#3. not : opposite of boolean value
print(not True)
print(not False)

print(10 and 20)   #research
print(10 or 20) 
# the and operator evaluates left to right and returns first false value it finds,
# if all values are true it returns the last value.
# the or operato evaluates left to right and returns the first true value it finda,
# if no true values are found ,it returns last value (which would be false).