from numpy import *

n = array(eval(input("Digite numero: ")))
num = 9

for i in n:
	if (i ==0):
		n[0] = n[0] - 1
	else: 
		n[1] =+1
print(n)
