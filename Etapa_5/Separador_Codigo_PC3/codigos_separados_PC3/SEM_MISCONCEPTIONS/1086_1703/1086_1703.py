#Hanna Soares Rodrigues - 21650885
#Avaliacao 02
#07/07/2016

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3)/ 3

print(round(media, 1))

if (media >= 7):
	print("Aprovado")
else:
	print("Reprovado")
	
	