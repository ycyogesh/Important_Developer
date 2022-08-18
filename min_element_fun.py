# Write a function that takes an array & return min element in it

a = [6,8,3,2,1]


def fmin(b):
    min = b[0]
    for i in range(0,len(b)):
            if(min>a[i]):
                min = a[i]
    return min

print(fmin(a))