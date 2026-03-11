tt = int(input("Quantidade de pontos tirados do troll: "))
ti = int(input("Quantidade inicial de forca do troll: "))
tr = int(input("Quantidade de forca recuperada pelo troll: "))
r = 1
soma = 0
while(tt < ti):
	ttr = ti - 5*tt
	ti = ttr + tr
	soma = soma + ti
	r = r + 1
print(r)