# Write a function that takes an array & return max element in it

a = [6,8,3,2,1]
max = 0

def fmax(b):
    for i in range(0,len(b)):
        max = a[0]
        for j in range(1,len(b)):
            if(max<a[j]):
                max = a[j]
    return max

print(fmax(a))