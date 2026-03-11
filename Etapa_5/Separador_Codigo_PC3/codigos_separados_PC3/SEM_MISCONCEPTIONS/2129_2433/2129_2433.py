from numpy import *
x = array(eval(input("Digite as notas: ")))

Mfinal = (x[0]*1 + x[1]*2 + x[2]*3 + x[3]*4)/10
print(round(Mfinal,2))

if Mfinal > 5:
	print("APROVADO")
else:
	print("REPROVADO")