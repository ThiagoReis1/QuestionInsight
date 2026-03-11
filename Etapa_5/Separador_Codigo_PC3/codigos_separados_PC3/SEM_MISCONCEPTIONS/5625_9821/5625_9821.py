ts = input("(T) se for tapioca (S) se for salgado:")
quant = float(input("quantidade de pedidos:"))
acai = float(input("quantidade de acai:"))

tapioca = (5.50 * quant + 10 * acai)
salgado = (4 * quant + 10 * acai)

if ts == ("T"):
	print (tapioca)
	
else:
	print(salgado)