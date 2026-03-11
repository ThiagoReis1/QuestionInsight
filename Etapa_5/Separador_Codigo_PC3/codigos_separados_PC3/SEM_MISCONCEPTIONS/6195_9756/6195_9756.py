numbac = int(input("Informe o numero de bacterias: "))
tx_cres = int(input("Informe a taxa de crescimento: "))
cthrs = 0
q = numbac
while q < numbac*2:
	q = q + (tx_cres/100)*q
	cthrs = cthrs + 1
print(cthrs)	