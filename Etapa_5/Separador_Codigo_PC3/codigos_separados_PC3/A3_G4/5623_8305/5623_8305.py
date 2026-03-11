c = input(" (B) se for bolo ou (S) se for salgado: ").upper()

q = int(input(" qual a quantidade de fatias: "))
y = int(input("quantidade de cappuccinos: "))

fb = 5.00
s = 4.00
cp = 7.50

total = 0

if c == "B":
	total = (q * fb + y * cp)
else:
	total = (q * s + y * cp)
	
print(round(total, 2))
