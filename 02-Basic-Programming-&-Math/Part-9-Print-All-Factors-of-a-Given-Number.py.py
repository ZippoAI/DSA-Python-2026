n = 10

num = n
store = []

for i in range(1, n+1):
    
    if n%i == 0:
        store.append(i)
    else:
        continue

print(store)