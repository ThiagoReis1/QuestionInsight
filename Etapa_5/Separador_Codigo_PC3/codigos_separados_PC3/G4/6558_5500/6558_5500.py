# faça seu código aqui!
# leia pontuacao do usuario
pu = int(input("Informe a pontuacao obtida: "))

# pontuacao limite 100
pl = 100

# condicao para verificar se menor que o limite
if pu < pl:
	# mensagem se menor que o limite
	print("eh menor")
# condicao para verificar se igual o limite
elif pu == pl:
	# mensagem se igual o limite
	print("eh limite")
# condicao se maior que o limite
else:
	# mensagem se maior que o limite
	print("eh maior")