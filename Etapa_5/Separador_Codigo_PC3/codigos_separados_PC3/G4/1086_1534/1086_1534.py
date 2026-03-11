#Instituto de computação-UFAM
#Suenne Renata Lima Fernandes- 21602342
#AV02- Exercício 01

a = float(input("Digite a nota:"))
b = float(input("Digite a nota:"))
c = float(input("Digite a nota:"))
nota = (( a + b + c)/3)
if (nota >= 7):
	print (round(nota,1))
	print ("Aprovado")
else:
	print (round(nota,1))
	print ("Reprovado")