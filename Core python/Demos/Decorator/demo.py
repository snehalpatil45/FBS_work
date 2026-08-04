def greet():
    print('Good Afternoon!')

fun = greet
del greet
fun()