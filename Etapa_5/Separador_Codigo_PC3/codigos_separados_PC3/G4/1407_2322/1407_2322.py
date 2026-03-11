vida = int(input("digite a vida inicial aqui: "))
D1 = int(input("digite o valor obtido no dado: "))
D2 = int(input("digite o valor obtido no dado: "))
D3 = int(input("digite o valor obtido no dado: "))
N = (D1 + D2 + D3)
dano = 10*N
if(vida - dano > 0):
	print(vida - dano)
	print("VIVO")
else:
	print("0")
	print("MORTO")