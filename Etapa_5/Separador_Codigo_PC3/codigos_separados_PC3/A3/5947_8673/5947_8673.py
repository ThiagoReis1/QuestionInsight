comida = input('C se for coxinha ou E se for esfirra: ')
qtd = float(input('insira a quantidade: '))
qtd_s = float(input('Insira a quantidade suco: '))

pf = 0.
 
if comida.upper() == 'C':
	pf = qtd * 2. + qtd_s * 6.
else:
	pf = qtd * 4.5 + qtd_s * 6
	
print(round(pf, 2))	


	


