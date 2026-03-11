s=float(input("quantidade de suco:"))
sal=float(input("quantidade de salgados:"))
dinheiro=float(input("valor disponivel:"))

suco=3.00
salgado=3.50

valortotal=(s*suco)+(sal*salgado)

if(dinheiro>=valortotal):
	mensagem="Sim"
else:
	mensagem="Nao"
	
print(round(valortotal, 2))
print(mensagem)
						