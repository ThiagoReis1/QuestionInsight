#Universidade Federal do Amazonas
#Thiago Tuma Camilo 21600549


premio = int(input("Digite o valor do prêmio recebido:"))
taxa = float(input("Digite o valor da taxa de rendimento:"))
ostentacao = int(input("Digite o valor da ostentação do rapaz:"))
meses = 0
grana = premio
while (grana > 0):
	grana = grana + (grana * taxa/100) - ostentacao
	meses = meses + 1

print (meses)
	