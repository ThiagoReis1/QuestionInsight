
from numpy import *

a = array(eval(input("insira: ")))
b = zeros(len(a),dtype = int) 
for i in range(len(a)):
	
		b[i] += a[i] +1

for i in range(len(b)):
	if(b[i] == 10):
		b[i] = 0
		
print(b)	