v = int(input("valor "))
j = float(input("juros "))
nv = v + (v/100*10)
t = 0
while (v > nv):
	saldo = v + (v/100*j)
	t = t + 1
print(t)