alt_m = 1.4
tx_m = 0.06

alt_l = float(input("insira a altura do leao: "))
tx_l = float(input("insira a taxa de crescimento do leao: "))

anos = 0

while alt_l >= alt_m:
	alt_m = alt_m + tx_m
	alt_l = alt_l + tx_l
	anos = anos + 1

print(anos)