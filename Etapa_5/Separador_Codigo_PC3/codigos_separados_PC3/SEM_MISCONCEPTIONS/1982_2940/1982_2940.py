pa = input('Informe o nome do país (Italia/Espanha): ')
cd = input('Informe o nome da cidade(Roma/Florenca/Frigiliana/Madrid): ')

###(((pa=='Italia')and(pa=='Espanha'))or ((cd='Roma')and(cd=='Florenca')and(cd=='Frigiliana')and(cd=='Madrid'))):


if(((pa=='Italia')or(pa=='Espanha')) and ((cd='Roma')or(cd=='Florenca')or(cd=='Frigiliana')or(cd=='Madrid'))):
	if((pa == 'Italia')and(cd == 'Roma')):
		print('latina'.upper())
	elif((pa= 'Italia') and (cd == 'Florenca')):
		print('siena'.upper())
	if((pa == 'Espanha') and (cd == 'Frigiliana')):
		print('malaga'.upper())
	else:
		if((pa == 'Espanha') and (cd == 'Madrid')):
			print('madrid'.upper()
else:
	print('provincia nao identificada'.upper())
  