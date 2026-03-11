nome = input("informe o nome do aminoacido:").upper()
o = 15.9994
c = 12.011
n = 14.00674
h = 1.00794
arginina = (c * 6) + (h * 15) + (n * 4) + (o * 2)
tirosina = (c * 9) + (h * 11) + (n * 1) + (o * 3)
triptofano = (c * 11) + (h * 11) + (n * 2) + (o * 2)
if(nome == "ARGININA"):
	print(round(arginina,2))
elif(nome == "TIROSINA"):
	print(round(tirosina,2))
elif(nome == "TRIPTOFANO"):
	print(round(triptofano,2))
else:
	print("Entrada: ", nome)
	print("Dado Invalido")