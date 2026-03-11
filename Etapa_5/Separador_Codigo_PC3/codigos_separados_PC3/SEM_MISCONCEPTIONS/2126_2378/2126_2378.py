from numpy import*

nota = array(eval(input("digite a nota: ")))

MFinal = (nota[0] * 5.0 + nota[1] * 2.5 + nota[2] * 2.5) / 10.0
print(round(MFinal, 2))

if(MFinal > 5):
	print("APROVADO")
else:
	print("REPROVADO")
