ge= input('Estilo do genêro musical.')
sub= input('O subgênero musical.')

if(ge.lower()=='vertente'and sub.lower()=='samba-de-raiz'):
	print('cavaquinho')
elif(ge.lower()=='vertente'and sub.lower()=='partido-alto'):
	print('surdo')
elif(ge.lower()=='misturado' and sub.lower()=='samba-choro'):
	print('violao de seis cordas')
elif(ge.lower()=='misturado'and sub.lower()=='samba-jazz'):
	print('saxofone')
else:
	print('instrumento nao identificado')

	