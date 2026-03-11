from numpy import*
notas = array(eval(input("")))
final =(notas[0]*5.0 + notas[1]*3 + notas[2]*2)/10
print(round(final, 2))
if (final >= 5):
	print("APROVADO")
else:
	print("REPROVADO")