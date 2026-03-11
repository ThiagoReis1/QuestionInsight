item = input("item: ")
quantidade = float(input("quantidade item:"))
quantidade_r = float(input("quantidade refrigerante: "))

L=5.00
s=3.50
re=4.00

x = L*quantidade + re*quantidade_r
y = s*quantidade + re*quantidade_r



if item=="L":
	print(round(x,2))
	
	
else:
	print(round(y,2))


