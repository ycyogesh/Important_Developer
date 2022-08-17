# Write a function that takes 2 arrays a & b and return all elemnts that are common in a & b

from tempfile import tempdir


a = [6,8,3,7,2,1]
b = [3,4,6,7,5]
temp =[]

def common(c,d):
    for i in range(0,len(c)):
        for j in range(0,len(d)):
            if(c[i]==d[j]):
                temp.append(c[i])
    return temp

print(common(a,b))