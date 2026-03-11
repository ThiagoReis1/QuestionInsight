a = float(input("Digite o numero de habitantes de Bravos: "))
b = float(input("Digite o numero de habitantes de Pentos: "))
c = float(input("Digite o numero de habitantes de Porto Real: "))
txa = float(input("Digite a taxa anual de crescimento da populacao de Bravos: "))
txb = float(input("Digite a taxa anual de crescimento da populaçao de Pentos: "))
txc = float(input("Digite a taxa anual de crescimento da populacao de Porto Real: "))
t = 1 


while ((a + b) < c):
	renda = a * (txa / 100)
	a = a +renda
	rendb = b * (txb / 100)
	b = b + rendb
	rendc = c * (txc / 100)
	c = c + rendc
	t = t + 1
print(t)