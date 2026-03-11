from numpy import *

n = array(eval(input("Informe os tempos: ")))

a = min(n)

i = 0

v = 0

while i < size(n):
	if(a == n[i]):
		v = i
		
	i = i + 1
		
print(v)