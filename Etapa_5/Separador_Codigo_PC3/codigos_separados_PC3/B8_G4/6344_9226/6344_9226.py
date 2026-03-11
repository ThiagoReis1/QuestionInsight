from numpy import* 

strg = input("Digite: ")

if strg[4] == "c" or strg[4] == "C":
	print(strg.upper())
elif strg[4] != "c" or strg[4] != "C":
	print("nome invalido")

