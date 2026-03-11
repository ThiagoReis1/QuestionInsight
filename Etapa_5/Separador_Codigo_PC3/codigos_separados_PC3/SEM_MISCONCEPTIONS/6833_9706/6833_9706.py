m = 7.25
p = 4.75
r = 3.50
compras = input().upper()

i = 0
total = 0

while i< len(compras):
	if compras[i] == "M":
		total = total + m
	if compras[i] == "P":
		total = total + p
	if compras[i] == "R":
		total = total + r
	i = i+1
print(round(total, 2))

