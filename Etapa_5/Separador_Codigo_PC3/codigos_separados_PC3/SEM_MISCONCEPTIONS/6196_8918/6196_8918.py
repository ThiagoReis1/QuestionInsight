altura_chico = 1.5
taxa_chico = 0.02
ap = float(input("Digite sua altura: "))
tc = float(input("Digite sua taxa anual de crescimento: "))

c = 0

while (ap < altura_chico):
	altura_chico = altura_chico + taxa_chico
	ap = ap + tc
	c = c + 1
print(c)