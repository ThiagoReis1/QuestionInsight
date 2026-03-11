from numpy import*
vet = array(eval(input("Notas das 3 atividades")))
NotaFinal = (vet[0]* 5.0 + vet[1] * 3.0 + vet[2] * 2.0) / 10.0
print(round(NotaFinal,2))
if(NotaFinal >= 5):
	print("APROVADO")
else:
	print("REPROVADO")