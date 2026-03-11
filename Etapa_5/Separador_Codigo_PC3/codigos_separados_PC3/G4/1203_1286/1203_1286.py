from numpy import *
v = array(eval(input()))
print(2.5)
i = 0
cont = 0
while(i<size(v)):
 if(v[i]>2.5):
  cont = cont+1
 i = i+1
print(cont)