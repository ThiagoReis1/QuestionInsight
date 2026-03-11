from numpy import *
n = array(eval(input()))
nf = (n[0] * 3.0 + n[1] * 3.0 + n[2] * 4.0)/10.0
print(round(nf,2))

if (nf >= 5.0):
	print("APROVADO")
else:
	print("REPROVADO")
