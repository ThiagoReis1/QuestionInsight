from numpy import*
notas = array (eval (input("digite as notas: ")))
n = ((notas[0] * 5) + (notas[1]*3) + (notas[2]*2)) / 10
print (round (n, 2))
if (n >= 5):
	print ("APROVADO")
else:
	print ("REPROVADO")