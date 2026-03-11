l = float(input("Digite o limite do cartao:"))
vc1 = float(input("Digite o valor da compra 1:"))
vc2 = float(input("Digite o valor da compra 2:"))
vc3 = float(input("Digite o valor da compra 3:"))
vc4 = float(input("Digite o valor da compra 4:"))

vt = vc1 + vc2 + vc3 + vc4

if (vt <= l):
	vt = vt
	m = "Dentro do limite"
else:
	m = "Estourou o limite"
	
print(round(vt, 2))
print(m)