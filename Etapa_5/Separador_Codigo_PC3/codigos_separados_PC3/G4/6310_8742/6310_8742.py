from numpy import*
opc = input("mercadoria: ").upper()
i = 0
m = 0
p = 0
r = 0
total = 0
while i < len(opc):
	if opc[i] == "M":
		m = m + 1
		total = total + 7.25
	if opc[i] == "P":
		p = p + 1
		total = total + 4.75
	if opc[i] == "R":
		r = r + 1
		total = total + 3.5
	i = i+1
print(round(total, 2))
print(m)
print(p)
print(r)
		