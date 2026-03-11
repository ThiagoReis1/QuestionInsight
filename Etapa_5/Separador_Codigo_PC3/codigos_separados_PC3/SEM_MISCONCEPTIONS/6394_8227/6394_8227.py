def codificar_mensagem(mensagem):
	codificada = []
	for numero in mensagem:
		proximo_numero =(numero + 1) % 10
		codificada.append(proximo_numero)
	return codificada

mensagem = input("digite:")
mensagem = list(map(int, mensagem.strip('[]').split(',')))

mensagem_codificada = codificar_mensagem(mensagem)

print('[{}]'.format(' '.join(map(str, mensagem_codificada))))