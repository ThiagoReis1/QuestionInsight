alt_m = 1.4
tx_m = 0.06
alt_l = float(input("Altura do Leao: "))
tx_l = float(input("Taxa de Cresc. Leao: "))

cont = 0

while alt_m <= alt_l:
	alt_m = alt_m + tx_m
	alt_l = alt_l + tx_l
	cont = cont + 1
print(cont)