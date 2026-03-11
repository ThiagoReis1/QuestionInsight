p1 = float(input("prova_1"))
p2 = float(input("prova_2"))
p3 = float(input("prova_3"))
np = (p1+p2+p3)/3
print(round(np,1))
if(np >= 7.0):
	mensagem = "Aprovado"
	print(mensagem)
else:
	mensagem = "Reprovado"
	print(mensagem)
	
