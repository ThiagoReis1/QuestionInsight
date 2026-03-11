from numpy import*
nota = array(eval(input()))
nf = (nota[0]*2 + nota[1]*3 + nota[2]*5)/10
print(round(nf,2))
if(nf>=5):
	print("APROVADO")
else:
	print("REPROVADO")