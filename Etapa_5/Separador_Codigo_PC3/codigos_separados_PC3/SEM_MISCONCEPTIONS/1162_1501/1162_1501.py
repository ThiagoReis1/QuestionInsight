premio = int(input("digite o valor do premio recebido: "))
taxa = float(input("digite o valor da taxa de rendimento: "))
ostentacao = int(input("digite o valor da ostentaçao: "))
meses = 0
grana = premio
while(grana>0):
	grana = grana + (grana * taxa/100) - ostentacao
	meses = meses + 1
	
print(meses)