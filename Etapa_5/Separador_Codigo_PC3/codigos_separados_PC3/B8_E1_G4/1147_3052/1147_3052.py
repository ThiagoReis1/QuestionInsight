X= str (input ('Nome da personagem: '))

	#Nome nao Listado
if (X != 'Daenerys') and (X != 'Cersei') and (X != 'Brienne') and (X != 'Arya') and (X != 'Sansa') and (X != 'Margaery') and (X != 'Catelyn') and (X != 'Meera'):
	print ('Entrada', X, 'invalida')
	
	#Tabela
elif (X == 'Daenerys'):
	print ('Aegon IV Targaryen')
elif (X == 'Cersei'):
	print ('Tywin Lannister')
elif (X == 'Brienne'):
	print ('Selwyn Tarth')
elif (X == 'Arya') or (X == 'Sansa'):
	print ('Eddard Stark')
elif (X == 'Margaery'):
	print ('Garth Tyrell')
elif (X == 'Catelyn'):
	print ('Hoster Tully')
elif (X == 'Meera'):
	print ('Howland Reed')