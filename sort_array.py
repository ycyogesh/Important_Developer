# Sort an array

a = [6,8,3,2,1]

for i in range(0,len(a)):
    min = a[i]
    minj = i
    for j in range(i+1,len(a)):
        if(a[j]<min):
            min = a[j]
            minj = j
    temp = a[i]
    a[i] = min
    a[minj] = temp
print(a)