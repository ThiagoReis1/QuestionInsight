p = input("Pais:")
c = input("cidade:")
if(p == 'Italia') and (c == 'Roma'):
	print('Latina'.upper())
elif(p == 'Italia') and (c == 'Florenca'):
	print('Siena'.upper())
elif(p == 'Espanha') and (c == 'Frigiliana'):
	print('Malaga'.upper())
elif(p == 'Espanha') and (c == 'Madrid'):
	print('Madri'.upper())
else:
	print('PROVINCIA NAO IDENTIFICADA'.upper())