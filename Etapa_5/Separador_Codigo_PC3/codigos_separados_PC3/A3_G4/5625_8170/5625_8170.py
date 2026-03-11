ts = input("T para tapioca ou S para salgado: ")
q = int(input("Quantidade: "))
qa = int(input("Quantidade de acais: "))

tapi = 5.50
salg = 4.00
acai = 10

pa = qa * acai

if (ts=="T"):
	y = (q*5.50) + (pa)
	print(round(y,2))
else:
	x = (q*4) + (pa)
	print(round(x,2))