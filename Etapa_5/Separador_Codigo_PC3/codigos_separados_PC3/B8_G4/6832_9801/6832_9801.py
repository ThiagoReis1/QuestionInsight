v = input("Produto? H/C/L ").upper()

i = 0
th = 0
tc = 0
tl = 0

while i < len(v):
	if v[i] == "H":
		th = th + 1
	elif v[i] == "C":
		tc = tc + 1
	elif v[i] == "L":
		tl = tl + 1
	i = i + 1
total = th * 5.4 + tc * 8.95 + tl * 4.5
print(round(total, 2))