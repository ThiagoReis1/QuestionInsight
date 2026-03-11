j = float(input("Digite j: "))
v = float(input("Digite v: "))
Q0 = 1500.00
t = 36
Qf = Q0 * ((1 + j)**t)
if (Qf >= v):
	M = "Sim"
else:
	M = "Nao"
print(round(Qf, 2))
print(M)