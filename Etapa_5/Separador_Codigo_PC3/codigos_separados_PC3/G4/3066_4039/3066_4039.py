pv=int(input())
d1=int(input())
d2=int(input())
d3=int(input())
p=10*(d1+d2+d3)
if((d1>12) or (d2>12) and (d3>12) or (pv<0)):
	print("Entrada invalida")
else:
	if(p<pv):
		print(pv-p)
		print("VIVO")
	else:
		print(0)
		print("MORTO")


