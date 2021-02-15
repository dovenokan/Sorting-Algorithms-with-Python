lst = [5,1,4,2,99,32,6,43,64,58,7,87,8]

for w in range(len(lst)-1):
    for n in range(len(lst)-1):
        if lst[n] > lst[n+1]: # > or <
            lst[n],lst[n+1] = lst[n+1],lst[n]

print(lst)
