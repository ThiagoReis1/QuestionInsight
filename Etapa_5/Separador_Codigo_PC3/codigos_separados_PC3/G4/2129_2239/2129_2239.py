from numpy import *
n = array(eval(input()))
m = (n[0]*1.0 + n[1]*2.0 + n[2]*3.0 + n[3]*4.0)/10.0

if m>=5:
	print(round(m,2))
	print("APROVADO")
else:
	print(round(m,2))
	print("REPROVADO")
 