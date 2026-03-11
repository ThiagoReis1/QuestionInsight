num_virus=int(input("Digite em A:"))
num_leuco= int(input("Digite em B:"))
taxa_virus= float(input("Percentual A:"))
taxa_leuco=float(input("Percentual B:"))

dias = 1
while(num_virus <= num_leuco):
	num_virus=num_viru + (num_virus * (taxa_virus/100))
	num_leuco= num_leuco + (num_leuco * (taxa_leuco/100))
	dias = dias + 1
print(dias)