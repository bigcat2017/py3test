# -*- coding: utf-8 -*-
import math


def isnumber(*numbers):
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError(" %s is not a number" % num)


def quardratic(a, b, c):
    isnumber([a, b, c])
    d = b * b - 4 * a * c
    if a == 0:
        if b == 0:
            if c == 0:
                return '方程根为全体实数'
            else:
                return "方程无根"
        else:
            x1 = -c / b
            x2 = x1
            return x1, x2
    else:
        if d < 0:
            return "方程无根"
        else:
            x1 = (-b + math.sqrt(d)) / 2 / a
            x2 = (-b - math.sqrt(d)) / 2 / a
            return x1, x2


def product(*args):
    if args is None or len(args) == 0:
        raise TypeError("arg not null")
    result = 1
    for arg in args:
        result = result * arg
    return result

print("result is %s " % product(5,6,10))
