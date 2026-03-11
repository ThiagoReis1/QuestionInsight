from dumpy import*

vet_num = eval(int(input("Digite valores entre 1 e 4: ")))
i = 0
pont = 10000

while (Anel == 1):
	x = pont * 2
	if (Anel == 2):
		x = pont
	if (Anel == 3):
		x = pont / 2
	if (Anel == 4):
		x = pont / 4
	i = i + x
print(round(x, 2))