#Aprovação
from numpy import*


notas= array(eval(input("Quais as notas: ")))
Notas0 = (notas[0])
Notas1 = (notas[1])
Notas2 = (notas[2])
peso1= Notas0 * 2
peso2 = Notas1 * 3
peso3 = Notas2 * 5

NF = (peso1+peso2+peso3)/10

						 
if (NF>=5):
	print(round(NF,2))
	print("APROVADO")
else:
	print(round(NF,2))
	print("REPROVADO")





