from numpy import*
v = array(eval(input("")))
nf = ((v[0]*2) + (v[1] * 3) + (v[2]*5))/10
print(round(nf,2))		
if (nf >= 5 ):
	print("APROVADO")
else:
	print("REPROVADO")		