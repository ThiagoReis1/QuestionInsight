sa = float(input("Digite o salario: "))
if (sa<1212):
	nv = sa + (0.12 * sa)
elif (sa>=1212) and (sa<=5000):
	nv = sa + (0.08 * sa)
elif (sa>5000):
	nv = sa + (0.03 * sa)
print(round(nv,2))