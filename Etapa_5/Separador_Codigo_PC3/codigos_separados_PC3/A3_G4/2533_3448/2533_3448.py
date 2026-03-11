qV = int(input("Valor da idenizacao:"))
qC = int(input("Valor do Saque Mensal:"))
cpJ = float(input("Taxa de Juros:"))
pcpV = qV / 1
pcpL = cpL / 100

tV = 0
tL = 0
d = 0

while (qL < (2 * qV)):
	qV = qV + (qV * pcpV)
	qL = qL + (qL * pcpL)
	tV = qV
	tL = qL
	d = d + 1
print(d)