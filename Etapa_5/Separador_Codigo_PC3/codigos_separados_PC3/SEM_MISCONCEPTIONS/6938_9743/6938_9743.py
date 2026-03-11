v = float(input("valor total da compra:"))
c = input("codigo da opcao de pagamento:")
p = v-v*(11/100)
d = v-v*(11/100)
c1 = v+v*(6/100)

if c == "d":
	print(round(d,2))
elif c == "p":
	print(round(p,2))
else:
a = int(input("1 ou 2:"))
	
	print(round(c1,2))