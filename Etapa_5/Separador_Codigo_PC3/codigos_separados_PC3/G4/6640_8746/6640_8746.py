# faça seu código aqui!
x = input("DIGITE: ").upper()

i = 0
x2 = 0

while i < len(x):
	if x[i] == "N":
		x2 = x2 + 1
	if x[i] != "N":
		print("nao achei")
	i = i + 1
print(x2)
	
