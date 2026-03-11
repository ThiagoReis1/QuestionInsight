nota1 = float(input("Insira a primeira nota:"))
nota2 = float(input("Insira a segunda nota:"))
nota3 = float(input("Insira a terceira nota:"))

nota4 = (nota1 + nota2 + nota3)/3

if(nota4>=7.0):
	media = "Aprovado"
else:
	media = "Reprovado"
print(round(nota4, 1))
print(media)