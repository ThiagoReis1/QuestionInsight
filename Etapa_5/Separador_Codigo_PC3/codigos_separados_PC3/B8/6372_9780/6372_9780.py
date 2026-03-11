from numpy import*

cat = zeros(4, dtype = int)
itens = input("coloque o produto: ").upper().split(",")

for i in itens:
	if i == "A":
		cat[0] += 1
	elif i == "B":
		cat[1] += 1
	elif i == "L":
		cat[2] += 1
	elif i == "H":
		cat[3] += 1
print (cat)