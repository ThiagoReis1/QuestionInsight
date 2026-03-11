from numpy import *
v = array(eval(input()))
i = 0
cont = 0
while(i<size(v)):
 if(v[i]>=0):
  cont= cont+1
 i=i+1

pos = array(zeros(cont,dtype=float))
i = 0
j = 0
while(i<size(v)):
 if(v[i]>=0):
  pos[j]=v[i]
  j = j+1
 i = i+1
print(pos)