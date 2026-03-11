nome=input("digite o nome: ")
d1=int(input("digite d1: "))
d2=int(input("digite d2: "))
d3=int(input("digite d3: "))
d4=int(input("digite d4: "))
if nome.lower()== "espada":
	mensagem = (d1+6+d2+6+d3+6+d4+6)
	print(mensagem)

if nome.lower()== "cauda":
	mensagem = (d1+d2+d3)*d4
	print(mensagem)
