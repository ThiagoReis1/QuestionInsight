from numpy import*
nota = array(eval(input(": ")))
nf = (nota[0]*5.0+nota[1]*3.0+nota[2]*2.0)/10
print(round(nf, 2))
if(nf>=5):
	print("APROVADO")
else:
	print("REPROVADO")
