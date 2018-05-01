#!/usr/bin/python3

from math import *

print("Calculate divisors of a number(https://www.practicepython.org/exercise/2014/02/26/04-divisors.html)");
num = input("Input a number: ")
num = int(num)

# notice: range(2, 5) equals list [2, 3, 4] and 5 is not included
i = 0
for i in range(2, int(sqrt(num))):
    if num % i == 0:
        print(i, int(num / i))  # divisor doesn't equal result
# divisor equals result
if (i + 1) == sqrt(num):
    print(i + 1)
