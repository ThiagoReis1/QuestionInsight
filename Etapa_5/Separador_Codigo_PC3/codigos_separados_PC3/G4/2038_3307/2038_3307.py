# Leitura da resposta
resp = input('Resposta: ').upper()

i = 0     # contador
soma = 0  # acumulador
while resp != 'S':
	if resp == 'SIM':
		soma = soma + 1
	i = i + 1
	resp = input('Resposta: ').upper()		
print(soma)
			
	