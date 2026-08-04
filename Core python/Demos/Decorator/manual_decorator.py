def greet():
    print('Good Afternoon!')

def myDecorator(fun):
    print('This is my decorator.')
    fun()
    print('End of my decorator.')

myDecorator(greet)