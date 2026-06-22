''' Method One'''

# n = 1634

# nod = len(str(n))

# num = n
# total = 0

# for i in str(num):
#     total = total + int(i)**nod 

# if total==n:
#     print('Armstrong')
# else:
#     print('Not armstrong')   

'''
Method Two

'''


n = 1634

power = len(str(n))
num = n
total = 0

while num>0:
    ld = num%10

    total+=ld**power
    num = num//10

if total==n:
    print('Armstrong')
else:
    print('Not armstrong')   
