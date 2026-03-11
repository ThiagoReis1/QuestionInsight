cm = input("O que voce deseja? Digite L para lanche, ou P para prato executivo ")
p= 13.50
ref= 3.00
l= 6.00

if(cm == "L"):
	qnt_L = int(input("Informe a quantidade de lanches que voce deseja: "))
	qnt_Ref = int(input("Informe a quantidade de refrigerantes voce deseja: "))
	total = float((qnt_L*l)+(qnt_Ref*ref))
else:
	qnt_P = int(input("Informe a quantidade de pratos que deseja: "))
	qnt_Ref = int(input("Informe a quantidade de refrigerantes que voce deeja: "))
	total = float((qnt_P*p)+(qnt_Ref*ref))
	
print(round(total,2))