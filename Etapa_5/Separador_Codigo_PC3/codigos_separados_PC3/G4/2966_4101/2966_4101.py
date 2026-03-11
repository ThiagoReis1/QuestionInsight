m = input()
p = float(input())
q = int(input())

pd = p - (0.2*p)

if (m == "S"):
	valor = (pd*q)
else:
	valor = (p*q)

print(round(valor, 2))	