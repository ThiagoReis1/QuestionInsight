from numpy import*

numero = input("Digite as notas: ").upper().split(",")
cat = zeros(4, dtype= int)

for i in numero:
	if i == "C":
		cat[0] += 1 
	elif i == "D":
		cat[1] += 1
	elif i == "V":
		cat[2] += 1
	elif i == "U":
		cat[3] += 1
		
print(cat)