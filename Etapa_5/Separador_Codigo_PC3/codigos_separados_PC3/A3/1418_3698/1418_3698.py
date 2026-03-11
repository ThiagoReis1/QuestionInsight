mais_votado = int(input('Votos do mais votado: '))
segundo_lugar = int(input('Votos do segundo lugar: '))
menos_votado = int(input('Votos do menos votado: '))
brancos = int(input('Votos em branco'))
nulos = int(input('Votos nulos: '))

if (mais_votado < 200000/2):
	mensagem = "sim"
else:
	mensagem = "nao"
	
print(mensagem.upper())