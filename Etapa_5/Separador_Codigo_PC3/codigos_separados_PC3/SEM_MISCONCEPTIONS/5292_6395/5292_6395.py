cor = input("digite:").upper()

preta = 0
vermelha = 0

while(cor != "S"):
	if(cor == "PRETA"):
	   preta = preta + 1
	if cor == "VERMELHA":
		vermelha = vermelha + 1
	cor = input("digite:").upper()
	
total = preta + vermelha 
print(total)
p = (preta * 100) / total
print(round(p,2))
	
	


