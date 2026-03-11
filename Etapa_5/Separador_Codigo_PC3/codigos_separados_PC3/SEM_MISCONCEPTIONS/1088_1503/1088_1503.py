nota1 = float(input("digite a nota da prova 1:"))
nota2 = float(input("digite a nota da prova 2:"))
nota3 = float(input("digite a nota da prova 3:"))
nota4 = float(input("digite a nota da prova 4:"))
nota5 = float(input("digite a nota da prova 5:"))

media = (nota1 + nota2 + nota3 + nota4 + nota5)/5
j = round(media, 2)
if ( j >= 7 ):
	m = "Aprovacao"
else:
	m = "Reprovacao"

print(j)
print(m)