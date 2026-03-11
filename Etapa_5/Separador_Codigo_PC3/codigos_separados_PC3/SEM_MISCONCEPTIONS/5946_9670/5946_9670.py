opcao= input("L para lanche P para pizza: (L/P)").upper()
qntopcao= int(input("quantidade de lanches ou pizzas: "))
qntrefri= int(input("quantidade de refrigerantes: "))

if opcao == "L":
	valor= qntopcao*6+qntrefri*3
else:
	valor= qntopcao*4.50+qntrefri*3

print(valor)
