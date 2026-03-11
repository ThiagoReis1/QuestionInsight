tempo = int(input())
lugar = input(). upper()

cal= 2023 - tempo

if lugar != 'B' and lugar != 'E':
	print('invalido')
elif(lugar == 'B' and cal >= 21):
	print('sim')
	print(cal - 21)
elif(lugar == 'B' and cal < 21):
	print('nao')
	print(21 - cal)
elif(lugar == 'E' and cal >= 18):
	print('sim')
	print(cal - 18)
else:
	print('nao')
	print(18 - cal)

