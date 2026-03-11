from numpy import*
veloc = array(eval(input("Digite a velocidade: ")))

limvel = veloc[0]
limin = limvel + (limvel *0.20)
limmax = limvel + (limvel * 0.50)


i = 1
for x in veloc[1:]:
	if(x > limin) and (x < limmax):
		print(i)
	i += 1

for u in veloc[1:2]:
	print(u)
	u += 0