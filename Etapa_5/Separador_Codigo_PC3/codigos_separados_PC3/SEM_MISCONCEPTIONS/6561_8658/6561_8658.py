# faça seu código aqui!
nv = int(input("numero voo: "))

if nv == 175:
	mensagem = "voo premiado"
elif nv < 175:
	mensagem = "eh menor"
else:
	mensagem = "eh maior"

print(mensagem)