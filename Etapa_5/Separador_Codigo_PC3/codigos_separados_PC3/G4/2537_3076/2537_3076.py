v = float(input("heranca: "))
s = float(input("saque: "))
j = float(input("juros por cento: "))

jpc = j/100
m = 0
sup = v + (v*20/100)

if (v>0 and s>0 and j>0):
	while (v<sup):
		v = round(v + (v * jpc), 2)
		v = rv - s
		m = m + 1
	print(m)
else:
	print("Dados incorretos.")