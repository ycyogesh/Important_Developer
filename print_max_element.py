# Print max element in a

a = [6,8,3,2,1]

max = 0
for i in range(0,len(a)):
    max = a[0]
    for j in range(1,len(a)):
        if(a[j]>max):
            max = a[j]
print(max)