a = int(input('Enter num 1:'))
b = int(input('Enter num 2:'))
try:
    res = a // b
    print(f'Result:{res}')
    # num = int(input('Enter the num'))
    # for i in num:
    #     print(i)

except ZeroDivisionError as s:
    print(f'code run with exception{s}')
except ValueError as v:
    print(f'I am value error.')
except Exception as e:
    print(f'Generalized exception {e}')
else:
    print('I am in else block')
finally:
    print('I am in finally block')