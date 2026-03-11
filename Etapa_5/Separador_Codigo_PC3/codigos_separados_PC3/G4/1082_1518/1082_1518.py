# universidade federal do amazonas
# aluno - Geovanni Vieira - 21453456
# data - 07/07/16  prova-02


# provas e aprovacao

n1 = float(input("digite a nota 1:"))
n2 = float(input("digite a nota 2:"))
n3 = float(input("digite a nota 3:"))
n4 = float(input("digite a nota 4:"))
n5 = float(input("digite a nota 5:"))

mf = (n1 + n2 + n3 + n4 + n5)/5

if (mf >= 5):
	print(round(mf,1))
	print("Aprovado")
else:
	print(round(mf,1))
	print("Reprovado")