qi = int(input("Qtd. inicial: "))
qc = int(input("Qtd. balões construídos: "))
qd = int(input("Qtc. balões destruídos: "))

t = 0

while (qi < 200):
	qi = (qi - qd) + qc
	saldo = qi
	t = t + 1
print(t)