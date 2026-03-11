p1=float(input("sua 1°prova?"))
p2=float(input("sua 2°prova?"))
p3=float(input("sua 3°prova?"))
p4=float(input("sua 4°prova?"))
p5=float(input("sua 5°prova?"))
nota= (p1+p2+p3+p4+p5) / 5
if(nota>= 5):
	print(round(nota,1))
	print("Aprovado")
else:
	print(round(nota,1))
	print("Reprovado")