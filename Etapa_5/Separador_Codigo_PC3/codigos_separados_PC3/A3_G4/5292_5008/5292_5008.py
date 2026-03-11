cor = input("cor: ")
p = 0
v = 0
x = 0
while (cor.upper()=="PRETA" or cor.upper()=="VERMELHA"):
	if (cor.upper()=="PRETA"):
		p += 1
	if (cor.upper()=="VERMELHA"):
		v += 1
	x += 1
	cor = input("cor: ")
print(x, round(100*p/x, 2))