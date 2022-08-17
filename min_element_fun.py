# Write a function that takes an array & return min element in it

a = [6,8,3,2,1]
min = 0

def fmin(b):
    for i in range(0,len(b)):
        min = a[0]
        for j in range(1,len(b)):
            if(min>a[j]):
                min = a[j]
    return min

print(fmin(a))