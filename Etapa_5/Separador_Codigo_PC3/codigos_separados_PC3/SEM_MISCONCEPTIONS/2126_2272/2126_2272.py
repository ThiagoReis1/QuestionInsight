from numpy import*

notas=array(eval(input("digite as notas")))

mp=(notas[0]*5+notas[1]*2.5+notas[2]*2.5)/10
print(round(mp,2))
if(mp>=5):
	print("APROVADO")
else:
	print("REPROVADO")
	