#Universidade Federal do Amazonas
#Suenne Renata Lima Fernandes-21602342
#Avaliação 02- Exercício01
#07/07/2016

a = float(input("Digite a primeira nota:"))
b = float(input("Digite a segunda nota:"))
c = float(input("Digite a terceira nota:"))
d = float(input("Digite a quarta nota:"))
ma =((a + b + c + d)/4)
if (ma >= 7):
	print(round(ma,2))
	print ("Aprovado")
	
else:
	print(round(ma,2))
	print ("Reprovado")