ataque= input("nome do ataque")
a = int(input("A"))
b = int(input("B"))

if(ataque== 'grito'):
	dano= 6+a+b
	print(dano)
else:
	dano= a**2 +2*a*b+ b**2
	print(dano)