pedido = input().upper()
quantidade1 = int(input())
quantidade2 = int(input())
bolo = 5
salgado = 4
cappuccino = 7.5

if pedido == "B":
	total = bolo * quantidade1 + cappuccino * quantidade2

if pedido == "S":
	total = salgado * quantidade1 + cappuccino * quantidade2
print(total)