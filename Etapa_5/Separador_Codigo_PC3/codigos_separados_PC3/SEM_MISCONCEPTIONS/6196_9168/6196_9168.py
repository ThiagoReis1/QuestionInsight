alt_fulano = float(input())
taxa_fu = float(input())

cont = 0
altura_chico = 1.5
taxa_chico = 0.02



while alt_fulano < altura_chico:
	
	alt_fulano += taxa_fu
	altura_chico += taxa_chico
	cont += 1		
print(cont)
	
	