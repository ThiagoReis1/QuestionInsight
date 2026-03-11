# faça seu código aqui!
palavra = input("Insira a palavra: ").upper()

i = 0

while i < len(palavra):
	if palavra[i] == "P":
		print(i)
	i += 1
	
if "P" not in palavra:
	print("nao achei")
