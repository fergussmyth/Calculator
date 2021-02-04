import time, math

print('Welcome to the most simple calculator!')
time.sleep(1)
print('Calculator starting..')
time.sleep(2)


def add(x, y):
    x + y


def subtract(x, y):
    x - y


def multiply(x, y):
    x * y


def division(x, y):
    x / y


print('Select on of the following')
print('1.Add')
print('2.Subtract')
print('3.Multiply')
print('4.Divide')
print('5.Square root')

while True:
    select = input('Enter your choice (1,2,3,4,5) : ')

    if select in ('1', '2', '3', '4'):
        num1 = float(input('Enter your first number:'))
        num2 = float(input('Enter your second number:'))
    if select == '5':
        num3 = float(input('Please enter your number:'))

        if select == '1':
            print(num1, '+', num2, '=', num1+num2)
        elif select == '2':
            print(num1, '-', num2, '=', num1-num2)
        elif select == '3':
            print(num1, '*', num2, '=', num1*num2)
        elif select == '4':
            print(num1, '/', num2, '=', num1/num2)
        elif select == '5':
            print('The square root of', num3, 'is:', math.sqrt(num3))
    else:
        print('Sorry, invalid input!')
