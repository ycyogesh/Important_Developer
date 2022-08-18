# Write a function that takes an array & return max element in it

a = [6,8,3,2,1]


def fmax(b):
    max = a[0]
    for i in range(0,len(b)):
        if(max<a[i]):
            max = a[i]
    return max

print(fmax(a))