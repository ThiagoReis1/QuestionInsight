qi = int(input("digite a quantidade inicial de pontos: "))

d1 = int(input("digite o valor de d1: "))
d2 = int(input("digite o valor de d2: "))
d3 = int(input("digite o valor de d3: "))
n = (d1 + d2 + d3)
pv = (qi - (n)*10) 
if (pv >= 0):
	msg1 = "VIVO"
	print(pv)
	print(msg1)
else:
	msg2 = "MORTO"
	print(pv)
	print(msg2)
	