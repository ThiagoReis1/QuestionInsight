rutra=int(input("Quantidade de votos Ambrosio Rutra:  "))
olecram=int(input("Quantidade de votos Demelza Olecram:  "))
votostotais=rutra+olecram
if (rutra>olecram):
	vencedor="Ambrosio Rutra"
	porcentagem=(rutra/votostotais)*100
else:
	vencedor="Demelza Olecram"
	porcentagem=(olecram/votostotais)*100
print(vencedor)
print(round(porcentagem, 2))