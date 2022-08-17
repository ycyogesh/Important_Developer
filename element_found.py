# Find a given element in array a print found / not found

a = [6,8,3,2,1]
n = int(input("Enter element to find : "))
flag = False

for i in range(0,len(a)):
    if(n == a[i]):
        flag = True
        break
if(flag):
    print("Element is Found")
else:
    print("Element is Not Found")