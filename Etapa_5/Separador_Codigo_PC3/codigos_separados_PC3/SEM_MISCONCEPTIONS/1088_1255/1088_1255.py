nota1 = float(input("valor da nota 1:"))
nota2 = float(input("valor da nota 2:"))
nota3 = float(input("valor da nota 3:"))
nota4 = float(input("valor da nota 4:"))
nota5 = float(input("valor da nora 5:"))
media = (nota1 + nota2 + nota3 + nota4 + nota5)/5
print(round(media,2))
if(media >=7):
	mensagem = "Aprovacao"
	
else:
	mensagem = "Reprovacao"
print(mensagem)
