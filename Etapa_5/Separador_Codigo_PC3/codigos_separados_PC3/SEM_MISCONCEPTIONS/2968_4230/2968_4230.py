Escolha= input("Lanche ou salgado? (L/S)")
qta= int(input())
qtb= int(input())

if(Escolha.upper()=="L"):
	Preço = qta*5 + qtb*4
else:
	Preço = qta*3.5 + qtb*4

print(round(Preço, 2))