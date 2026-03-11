consumo = float(input("consumo de agua em m3: "))
tfx = 30.00

if (consumo < 10):
	vc = 3 * consumo + tfx
else:
	vc = 3.5 * consumo + tfx
	
print(vc)