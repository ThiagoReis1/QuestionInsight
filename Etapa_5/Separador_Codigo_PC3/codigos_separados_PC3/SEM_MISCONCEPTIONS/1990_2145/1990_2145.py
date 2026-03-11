amino = input("Digite o nome do aminoacido: (GLUTAMINA/SERINA/TREONINA)")

o = 15.9994
c = 12.011
n = 14.0067
h = 1.00794

if (amino.upper() == "GLUTAMINA"):
	soma1 = (c * 5) + (h * 8) + (n * 1) + (o * 4)
	print(round(soma1,2))
elif (amino.upper() == "SERINA"):
	soma2 = (c * 3) + (h * 7) + n + (o * 3)
	print(round(soma2,2))
elif(amino.upper() == "TREONINA"):
	soma3 = (c * 4) + (h * 9) + n + (o * 3)
	print(round(soma3,2))
else:
	print("Entrada: ", amino)
	print("Dado Invalido")