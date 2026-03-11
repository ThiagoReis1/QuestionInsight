unidade = input("unidade: ").upper()
valor_vel = float(input("Valor da velocidade: "))

vkm = 3.6 * valor_vel
vms = valor_vel / 3.6

if (unidade == "K"):
	print(round(vms, 2))
else:
	print(round(vkm, 2))