from math import*
vo = int(input("digite o volume inicial: "))
vb = int(input("volume bombardiado: "))
vr = int(input("volume retirado: "))
i = 0
soma = 0
while (soma <= 1000):
	soma = soma + (vo + vb - vr)
	i = i + 1
print(i)
	