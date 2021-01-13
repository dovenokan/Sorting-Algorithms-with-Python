lst = [5,1,4,2,99,32,6,43,64,58,7,87,8]

for n in range(len(lst)):
    for i in lst:
        if i < lst[n]:
            lst[n],lst[lst.index(i)] = i,lst[n]
            print(lst)

print("Son",lst)