quant0 = int(input())
d1 = int(input())
d2 = int(input())
d3 = int(input())
N = d1 + d2 + d3
quantF = quant0 - (10 * N)
if (quantF > 0):
	print(quant0 - (10 * N))
	print("VIVO")
else:
	print(0)
	print("MORTO")
	
