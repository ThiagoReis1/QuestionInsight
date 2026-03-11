q = int(input("insira:"))
d = int(input("insira:"))
qm = int(input("isnira:"))
qr = int(input("insira:"))

i = 0
moedas = 0

while(q>0):
	moedas = qm - d - qr
	q = q + moedas
	i = i + 1

print(i)