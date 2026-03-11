from numpy import *

v = array(eval(input("Digite: ")))
cont = zeros(size(v), dtype = int)

for i in range(size(v), -1,-1):
	cont = v[i] -1 

print(cont)
	
	
	
	
	