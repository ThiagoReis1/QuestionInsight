Nota1 = float(input("digite Nota1:"))
Nota2 = float(input("digite Nota2:"))
Nota3 = float(input("digite Nota3:"))
Nota4= float(input("digite Nota4:"))

Soma = (Nota1+Nota2+Nota3+Nota4)

Media = Soma / 4

print(round(Media,1))

if (Media>=6):
	print("Aprovado")
if (Media<6):
	print("Reprovado")
