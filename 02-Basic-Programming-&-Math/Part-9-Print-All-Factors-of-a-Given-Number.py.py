# method 1

n = 10

num = n
store = []

for i in range(1, n+1):
    
    if n%i == 0:
        store.append(i)
    else:
        continue
print()
print('Brute Solution')
print(store)

  
# method 2

n = 10

num = n

result = []

for i in range(1, num//2+1):
    if num%i==0:
        result.append(i)
result.append(num)
print()
print('Better Solution')
print(result)


# ------------------ METHOD 3------------------------
from math import sqrt
n = 36
num = n
result = []

for i in range(1, int(sqrt(num))+1):
    if num%i==0:
        result.append(i)
        if num//i !=i:
            result.append(num//i)
print()
print('Optimal Solution')
print(sorted(result))