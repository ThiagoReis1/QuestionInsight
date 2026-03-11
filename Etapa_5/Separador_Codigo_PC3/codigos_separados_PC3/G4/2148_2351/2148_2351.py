from numpy import*
from math import *

vet= array(eval(input()))
print(sum(vet))
 
t=0
for i in range (size(vet)):
	if(vet[i] >= 5):
		t=t+1
print(t)