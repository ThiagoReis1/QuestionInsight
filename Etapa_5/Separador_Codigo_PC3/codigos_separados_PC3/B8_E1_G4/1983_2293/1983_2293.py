c = input("continente: ")
p = input("pais: ")
if((c.lower() != 'asia') and (c.lower() != 'america-do-sul') and (p.lower() != 'jordania') and (p.lower() != 'india') and (p.lower() != 'peru') and (p.lower() != 'brasil')):
	print('informacao nao identificada'.upper())
else:
	if (c.lower() == 'asia') and (p.lower() == 'jordania'):
	   print("as ruinas de petra".upper())
	elif((c.lower() == 'asia') and (p.lower() == 'india')):
		print("taj mahal".upper())
	elif (c.lower() == 'america-do-sul') and (p.lower() == 'peru'):
		print('MACHU PICCHU')
	elif (c.lower() == 'america-do-sul') and (p.lower() == 'brasil'):
		print('cristo redentor'.upper())
	