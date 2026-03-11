from numpy import *

st = input('Insira as nacionalidades:').split(',')
n = array(eval(input()))
v = zeros(size(n),dtype=int)

for i in range (size(st)):
	AR = 0
   BR = 0
   CL = 0
   CO = 0
   UY = 0
	

print(st)