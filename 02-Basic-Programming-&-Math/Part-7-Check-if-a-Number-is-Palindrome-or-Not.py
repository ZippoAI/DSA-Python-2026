# Part 7: Check if a Number is Palindrome or Not


n = 567765
num = n
result = 0
while num>0:
    ld= num%10
    result = result*10 + ld
    num = num//10

if result==n:
    print('Palindrome')
else:
    print('Not palindrome')
    


# Time Complexity = O(log10(N))
# Space Complecity = O(1)




