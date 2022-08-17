# Print min element in a

a = [6,8,3,2,1]

min = 0
for i in range(0,len(a)):
    min = a[0]
    for j in range(1,len(a)):
        if(a[j]<min):
            min = a[j]
print(min)