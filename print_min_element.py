# Print min element in a

a = [6,8,3,2,1]

min = 0
for i in range(0,len(a)):
    min = a[0]
    if(a[i]<min):
        min = a[i]
print(min)