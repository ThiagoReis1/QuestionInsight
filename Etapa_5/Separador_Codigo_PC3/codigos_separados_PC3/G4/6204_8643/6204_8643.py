altm = 1.86
taxam = 0.01

alt = float(input(":"))
taxa = float(input(":"))
ano = 0 

while(altm >= alt):
	alt = alt + taxa
	altm = altm + taxam
	ano = ano + 1
print(ano)
	
	
	