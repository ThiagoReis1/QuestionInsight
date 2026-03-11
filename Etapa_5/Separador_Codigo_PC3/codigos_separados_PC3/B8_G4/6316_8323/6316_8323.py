v = input().upper()

i = 0
qd = 0
qs = 0
qi = 0
price = 0

while i < len(v):
	if v[i] == "D":
		price = price + 2.25
		qd = qd + 1
	elif v[i] == "S":
		price = price + 4
		qs = qs + 1
	elif v[i] == "I":
		price = price + 6.90
		qi = qi + 1
	i = i + 1
print(round(price, 2), qd, qs, qi)