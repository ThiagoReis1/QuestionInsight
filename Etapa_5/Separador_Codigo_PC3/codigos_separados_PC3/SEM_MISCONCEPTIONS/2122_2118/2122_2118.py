from numpy import*

notas = array(eval(input()))

nf = (notas[0]*2.0+notas[1]*3.0+notas[2]*5.0)/10.0

print(round(nf,2))

if(nf>=5.0):
	print("APROVADO")
	
else:
	print("REPROVADO")
