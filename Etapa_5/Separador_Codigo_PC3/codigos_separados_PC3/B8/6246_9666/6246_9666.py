vitorias_A = 0


while True:
	entrada = input().upper()
	
	if entrada == 'A': vitorias_A += 1
	elif entrada == 'X': break
		
print(vitorias_A)
	