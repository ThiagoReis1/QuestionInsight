j=float(input())
v=int(input())

Qf=1500*((1+j)**36)
if(Qf>=v):
	print(round(Qf, 2))
	print("Sim")
else:
	print(round(Qf, 2))
	print("Nao")