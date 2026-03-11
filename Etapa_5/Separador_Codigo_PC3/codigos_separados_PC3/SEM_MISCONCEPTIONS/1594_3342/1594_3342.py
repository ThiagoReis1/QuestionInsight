from numpy import *

danos = array(eval(input("Danos: ")))
t=0
for i in range(size(danos)):
   t=t+(i+1)*danos[i]
print(t)	






