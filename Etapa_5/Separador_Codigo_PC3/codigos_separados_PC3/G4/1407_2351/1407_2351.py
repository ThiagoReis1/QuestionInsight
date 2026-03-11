quant_inicial= int(input())
d1= int(input())
d2= int(input())
d3= int(input())

n = 10 * (d1 + d2 + d3)

if (quant_inicial > n):
	x = (quant_inicial - n)
	print(x)
	print("vivo".upper())
	
else:
	print(0)
	print("morto".upper())
