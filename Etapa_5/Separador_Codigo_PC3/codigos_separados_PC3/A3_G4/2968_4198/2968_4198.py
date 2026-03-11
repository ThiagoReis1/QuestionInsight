L= input("Digite o pedido: ")
S= int(input("Digite a quantidade de lanches ou salgados: "))
qr= int(input("Digite a quantidade de refrigerantes: "))
pl= 5.00
ps= 3.50
pr= 4.00
if(L=="L"):
	total=pl+(S*ps)+pr
else:
	total=ps+pr
print(round(total,2))
