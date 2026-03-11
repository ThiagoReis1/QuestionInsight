# faça seu código aqui!
n = input("").upper()
i = 0
if "N" not in n:
	print("nao achei")
else:
	while i < len(n):
		if n[i] == "N":
			print(i)
		i+= 1