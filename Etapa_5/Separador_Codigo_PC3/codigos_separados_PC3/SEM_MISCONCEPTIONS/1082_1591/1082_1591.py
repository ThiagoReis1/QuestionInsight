nota1=float(input())
nota2=float(input())
nota3=float(input())
nota4=float(input())
nota5=float(input())

ma = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

if(ma >= 5):
	print(round(ma, 1))
	print("Aprovado")
	
else:
	print(round(ma, 1))
	print("Reprovado")
	