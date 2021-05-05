# import logging
from string import Template

def add(*args):
    add = 0
    for i in args:
        add += i
    return add

def subtract(*args):
    sub = 0
    for i in args:
        sub -= i
    return abs(sub)

def multi(*args):
    multi = 1
    for i in args:
        multi *= i
    return multi

def divide(*args):
    div = 1
    for i in args:
        div /= i
    return div

if __name__ == '__main__':
    num1 = 10
    num2 = 5
    
    add_r = add(num1, num2)
    print(f'Add: {num1} + {num2} = {add_r}')

    sub_r = subtract(num1, num2)
    print(f'Subtract: {num1} - {num2} = {sub_r}')

    multi_r = multi(num1, num2)
    print(f'Multi: {num1} * {num2} = {multi_r}')

    div_r = divide(num1, num2)
    print(f'Divide: {num1} / {num2} = {div_r}')

