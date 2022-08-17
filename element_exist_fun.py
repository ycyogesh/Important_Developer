# Write a function takes an array & an element and returns true/false based on the element exist or not

a = [6,8,3,2,1]
flag = False

def found(b):
    for i in range(0,len(b)):
        if(n == b[i]):
            return True
n = int(input("Enter Element : "))
if(found(a)):
    print("True")
else:
    print("False")