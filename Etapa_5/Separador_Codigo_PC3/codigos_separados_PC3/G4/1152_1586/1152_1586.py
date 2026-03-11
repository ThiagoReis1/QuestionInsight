a = float(input("Quantos habitantes tem a cidade A?"))
b = float(input("Quantos habitantes tem a cidade B?"))
c = float(input("Quantos habitantes tem a cidade C?"))
txa = float(input("Qual a taxa de A?"))
txb = float(input("Qual a taxa de B?"))
txc = float(input("Qual a taxa de C?"))
t = 1
while((a + b) < c):
	renda = a * (txa / 100)
	a = a + renda
	rendb = b * (txb/ 100)
	b = b + rendb
	rendc = c * (txc/100)
	c = c + rendc
	t = t +1
print(t)
