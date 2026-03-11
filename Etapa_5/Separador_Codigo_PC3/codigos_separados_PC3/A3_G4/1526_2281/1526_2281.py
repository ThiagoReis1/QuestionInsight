m = int(input("Quantidade inicial de mana: "))
qg = int(input("Quantidade gasta por dia: "))
qr = int(input("Quantidade de mana recuperada: "))
t = 0
soma = 0

while(m> 0 ):
	m = m -qg + qr
	t = t+1
print(t)