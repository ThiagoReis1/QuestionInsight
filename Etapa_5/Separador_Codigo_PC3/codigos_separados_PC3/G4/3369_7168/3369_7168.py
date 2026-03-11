uni = input("qual a unidade (M/K): ")
v = float(input("Qual a velocidade: "))

if(uni.upper() == "M"):
	Vkm = 3.6 * v
	print(round(Vkm, 2))
else:
	Vms = v / 3.6
	print(round(Vms, 2))
