quant = int(input("Digite a quantidade inicial:"))
d1 = int(input("Digite o valor de d1:"))
d2 = int(input("Digite o valor de d2:"))
d3 = int(input("Digite o valor de d3:"))

N = (d1 + d2 +d3) 
jog = 10* N

if (quant > jog):
	msg = "VIVO"
	print (quant - jog)
	print (msg)
	
else:
	msg = "MORTO"
	print (0)
	print (msg)