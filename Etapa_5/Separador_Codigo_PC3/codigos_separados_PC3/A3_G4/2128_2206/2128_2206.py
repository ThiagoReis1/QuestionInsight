from numpy import *

n = array(eval(input("")))

i = 0 
n1 = n[0]
n2 = n[1]
n3 = n[2]
n4 = n[3]
mn = n1 + n2 + n3 + n4 - max(n)

nf = (mn) / 3.0

if(nf >= 50.0):
	msg = "APROVADO"
else:
	msg = "REPROVADO"
	
print(round(nf, 2))
print(msg)
