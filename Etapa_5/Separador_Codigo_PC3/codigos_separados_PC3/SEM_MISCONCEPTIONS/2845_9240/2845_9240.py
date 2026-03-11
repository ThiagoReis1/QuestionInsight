entrada = input("Digite os numeros: ")

numeros = list(map(int, entrada[1:-1].split(',' )))

for i	in range(len(numeros)):
	if	numeros[i] == 9:
			numeros[i] = 0
	else:
		numeros[i] += 1
		
print('[' + ' '.join(map(str, numeros)) + ']')