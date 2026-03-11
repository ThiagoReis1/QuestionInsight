def codigo_secreto(vetor):
	resultado = []
	for numero in vetor:
		if numero == 9:
			resultado.append(0)
		else:
			resultado.append((numero + 1) ** 3)
	return resultado

entrada = [3, 5, 6, 1, 2, 0]
saida = codigo_secreto(entrada)
saida_formatada = ','.join(str(num) for num in saida)
print(saida_formatada)