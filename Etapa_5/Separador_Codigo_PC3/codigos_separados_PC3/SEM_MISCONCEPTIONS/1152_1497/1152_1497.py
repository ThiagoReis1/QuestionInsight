bravo = int(input(""))
pentos = int(input(""))
porto = int(input(""))
taxabravo = float(input(""))
taxapentos = float(input(""))
taxaporto = float(input(""))
anos = 0

while(bravo + pentos < porto):
	bravo = bravo + (bravo * taxabravo/100)
	pentos = pentos + (pentos * taxapentos/100)
	porto = porto + (porto * taxaporto/100)
	anos = anos +  1
print(anos)