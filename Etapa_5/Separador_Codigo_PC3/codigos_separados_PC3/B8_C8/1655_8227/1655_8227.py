string_estado = input("digite:")

estados = string_estado.split(',')

contagem = [0,0,0,0,0]

for estado in estados:
	estado = estado.strip().upper()
	if estado == 'AC':
		contagem[0] += 1
	elif estado == 'AM':
		contagem[1] += 1
	elif estado == 'PA':
		contagem[2] += 1
	elif estado == 'RO':
		contagem[3] += 1
	elif estado == 'RR':
		contagem[4] += 1
		
maior_quantidade = max(contagem)

print(maior_quantidade)
print('[' + ' '.join(map(str, contagem)) + ']')