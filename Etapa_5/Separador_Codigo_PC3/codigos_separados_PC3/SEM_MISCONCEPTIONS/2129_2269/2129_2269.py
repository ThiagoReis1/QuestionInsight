from numpy import*
notas = array(eval(input(": ")))
mf = (notas[0] * 1 + notas [1] * 2 + notas[2] * 3 + notas [3]*4)/10
print(round(mf, 2))
if(mf >= 5):
	print("APROVADO")
else:
	print("REPROVADO")
	