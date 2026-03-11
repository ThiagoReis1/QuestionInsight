#Universidade Federal do Amazonas- icomp
#Suenne Renata Lima Fernandes- 21602342
#Avaliacao 04
z = int(input("Quantidade de zumbis que invadiram?"))
h = int(input("Quantidade de habitantes"))
x = int(input("Quantidade de pessoas transformadas"))
y = int(input("Quantos zumbis são mortos por dia?"))
d = 0
while(h > 0):
	z = z * x
	z = z - y
	h = h - z
	d = d + 1
print(d)