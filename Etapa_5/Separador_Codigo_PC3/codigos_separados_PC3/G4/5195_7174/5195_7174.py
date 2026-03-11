d=float(input("distancia em km da corrida:  "))
ck=float(input("chakra restante:  "))

d= d*1000
ckn = (d/10)*30
if(ck>=ckn):
	print(round(ckn, 2))
	print("vai conseguir")
else:
	print(round(ckn, 2))
	print("nao vai conseguir")
