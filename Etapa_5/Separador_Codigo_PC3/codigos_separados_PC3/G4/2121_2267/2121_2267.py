from numpy import*
n = array(eval(input("")))
pf = (n[0] * 5 + n[1] * 3 + n[2] * 2)/10.0
print(round(pf, 2))
if(pf>=5):
	x = "APROVADO"
else:
	x = "REPROVADO"
print(x)
	
