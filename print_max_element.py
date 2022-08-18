# Print max element in a

a = [6,8,3,2,1]

max = a[0]
for i in range(0,len(a)):
    if(a[i]>max):
        max = a[i]
print(max)