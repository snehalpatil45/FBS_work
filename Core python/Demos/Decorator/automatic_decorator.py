def myDecorator(fun):
    # print('This is my decorator')
    def wrapper():
        print('This is wrapper function')
        fun()
        print('End of wrapper function')
    return wrapper


@myDecorator
def greet():
    print('Good Afternoon!')

greet()
# fun = greet()
# greet = none
# greet = wrapper