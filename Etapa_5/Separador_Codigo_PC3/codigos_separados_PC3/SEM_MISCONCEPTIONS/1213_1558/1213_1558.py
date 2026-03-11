from numpy import *
v = array(eval(input("Digite o peso dos levantamentos----> ")))
recorde = 217
n = 0
i = 0
while(i < size(v)):
   if(v[i] > recorde):
		n = n + 1
print(recorde)	
print(n)
