nota1=float(input("prova1: "))
nota2=float(input("prova2: "))
nota3=float(input("prova3: "))
nota4=float(input("prova4: "))
nota5=float(input("prova5: "))

notas=(nota1+nota2+nota3+nota4+nota5)
N=notas/5

if(N>=5):
	print(round(N,1))
	print("Aprovado")
else:
	print(round(N,1))
	print("Reprovado")
	
	