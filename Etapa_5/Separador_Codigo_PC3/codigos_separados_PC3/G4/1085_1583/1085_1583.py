A = float(input("Qual a nota da prova 1? "))
B = float(input("Qual a nota da prova 2? "))
C = float(input("Qual a nota da prova 3? "))
D = float(input("Qual a nota da prova 4? "))
E = float(input("Qual a nota da prova 5? "))

media_aritmetica = (A+B+C+D+E)/5.0
if(media_aritmetica >= 6):
	print(round(media_aritmetica,2.0))
	print("Aprovado")
else:
	print("Reprovado")
print