# faça seu código aqui!
t = input("digite o tipo do combo (A, B ou C): ").upper()
q = int(input("Digite a qtd de combos desejada: "))

v = 30.00
vt = q * v

if(t == "C"):
	d = vt - (vt*15/100)
	print(d)
else:
	print(vt)