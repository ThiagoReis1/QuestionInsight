num = int(input("Digite o numero de votos: "))
cont = 0
l = 0
c = 0
p = 0

while cont != num:
	cont += 1
	esc = input("Vote agora: Churrasco(C), Panquecas(P) ou Lasanha(L)? ").upper()
	if esc == "C":
		c += 1
	elif esc == "P":
		p += 1
	elif esc == "L":
		l += 1

print("L=", l)
print("C=", c)
print("P=", p)