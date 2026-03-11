from numpy import*
n= array(eval(input()))

af = (n[0]*3.0 + n[1]*2.0 + n[2]*2.0 + n[3]*3.0)/10.0
print(round(af,2))
if (af >= 5.0):
	print("APROVADO")
else:
	print("REPROVADO")