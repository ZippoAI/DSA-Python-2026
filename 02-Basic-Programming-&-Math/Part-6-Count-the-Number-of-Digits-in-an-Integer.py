# Part 6: Count the Number of Digits in an Integer


n = 5873

num = n
count = 0
while num>0:
    num = num//10
    count +=1

print(count) 


# ANOTHER WAY

from math import *

def countDigit(num):
    return int((log10(num)+1))


print('Lengh of N is : ', countDigit(n))