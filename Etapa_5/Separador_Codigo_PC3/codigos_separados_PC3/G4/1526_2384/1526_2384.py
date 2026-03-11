q = int(input("Insira a quantidade incial de mana: "))
qg = int(input("Quantidade de mana gasta por dia: "))
qr = int(input("Quantidade de mana recuperada durante o sono: "))
d = 0


while(q > 0):
	q = q - qg + qr
	d = d + 1
print(d)