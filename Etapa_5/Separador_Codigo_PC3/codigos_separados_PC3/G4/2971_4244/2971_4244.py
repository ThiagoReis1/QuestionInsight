j = float(input())
v = float(input())

Q = float(1500.00)
t = 36

Qf = Q*(1+j)**t

if(v>=Qf):
	print(round(Qf, 2))
	print("Nao")
else:
	print(round(Qf, 2))
	print("Sim")
