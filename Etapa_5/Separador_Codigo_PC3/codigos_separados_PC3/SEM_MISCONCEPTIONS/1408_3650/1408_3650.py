arma = input('nome da arma')
destreza = float(input('destreza'))
dado1 = int(input('dois valores sorteados'))
dado2= int(input('dois valores sorteados'))
katana = (2*(dado1+dado2))+destreza
sabre = (dado1+dado2)+ (2*destreza)
if(arma =='katana'):
	print(katana)
else:
	print(sabre)