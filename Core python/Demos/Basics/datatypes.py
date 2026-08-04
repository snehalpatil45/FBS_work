### Data types
# overwrite - replacing something that already exists with a new value
# Garbage collector - when reference count is less than one then memory is frees or remove
# comment - used for documentation ,neither translated never executed

## Numeric:
# 1. int
x = 10         #variable initilization
# 2. float 
x = 3.14
# 3. complex
x = 10 + 5j

##Text:
#1. str
x = 'Snehal'
x = "snehal's"
x = '''firstbit solution'''
x = """this is first line 
this is second line"""

##sequential:
#1.list
x = [ 10,20,30 ]
#2. tuple
x = ( 10,20,30 )
#3. range
x = range( 1,10 )

##settype:
#1.set
x = { 10,20,30 }
#2. frozenset
x = frozenset({ 10,20,30 })

##Mapping:
#1.dict
x = {1:'python',2:'java'}

##Boolean:
#1.bool
x = True #x=false

##nonetype
x = None
print(type(x))