m=int(input("insira quantidade de mana inicial: "))
p=int(input("quantidade perdida por dia: "))
g=int(input("quauantidade ganha ao dormir: "))


d=0

while(m > 0):
	m=m - p + g
	d=d+1
print(d)