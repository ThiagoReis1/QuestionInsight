caraOUcoroa = input("Cara ou coroa?").upper()
numeroJogadas = 0
qtdCaras= 0 
while caraOUcoroa != 'S':
	if caraOUcoroa == 'CARA':
		qtdCaras = qtdCaras + 1
	caraOUcoroa = input("Cara ou coroa?").upper()
	
print(qtdCaras)