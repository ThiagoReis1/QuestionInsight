p = input("digite o pedido: ")
qtd = int(input("digite a quantidade: "))
qtd_r = int(input("digite a quantidade de refrigerantes: "))
L = 5.0
S = 3.5
R = 4.0

if p == "L":
	print(round(L * qtd + R * qtd_r,2))
else: 
	print(round(S * qtd + R * qtd_r,2))