j = float(input("Juros: "))
v = float(input("Valor: "))
Q0= 1500 
t = 36
Qf= Q0 * ((1 + j)**t)
if(Qf>=v):
	print(round(Qf,2))
	print("Sim")
else:
	print(round(Qf,2))
	print("Nao")