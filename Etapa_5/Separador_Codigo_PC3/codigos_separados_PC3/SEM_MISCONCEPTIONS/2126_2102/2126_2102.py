from numpy import*

notas=array(eval(input()))

mf=(notas[0]*5 + notas[1]*2.5 + notas[2]*2.5)/10.0

print(round(mf,2))
if(mf>5.0):
	print("APROVADO")
else:
	print("REPROVADO")
	