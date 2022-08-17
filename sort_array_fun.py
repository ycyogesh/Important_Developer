# Write a function that takes an array a & return the sorted array

a = [6,8,3,2,1]

def sort(b):
    for i in range(0,len(b)):
        min = b[i]
        minj = i
        for j in range(i+1,len(b)):
            if(min>a[j]):
                min = b[j]
                minj = j
        temp = b[i]
        b[i] = min
        b[minj] = temp
    return b

print(sort(a))