from numpy import*

letras = input(("")).upper()
i = 0

while i < len(letras):
	if letras[i] == "L":
		print(i)
	i = i +1
if "L" not in letras:
	print("nao achei")