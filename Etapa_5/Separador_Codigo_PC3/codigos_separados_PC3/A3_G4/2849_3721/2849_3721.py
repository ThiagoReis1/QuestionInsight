from numpy import *

a = array(eval(input("Notas:")))

s = 0

for i in range(size(a)):
    if a[i] == 0:
        s = 0
    else:
        s+=a[i]

print(s)


