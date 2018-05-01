#!/usr/bin/python3

from math import *

print("Calculate divisors of a number(https://www.practicepython.org/exercise/2014/02/26/04-divisors.html)");
num = input("Input a number: ")
num = int(num)

for i in range(2, ceil(sqrt(num))):
    if num % i == 0:
        print(str(i) + " " + str(int(num / i)))
