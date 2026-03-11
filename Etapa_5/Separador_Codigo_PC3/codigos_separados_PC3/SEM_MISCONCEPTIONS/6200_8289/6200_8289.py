altura_max = 1.75
taxa_max = 0.01

novo = float(input(":"))
novotaxa = float(input(":"))

acum = 0
while altura_max > novo :
	altura_max = altura_max + taxa_max
	novo = novo + novotaxa
	acum +=1 
print(acum)