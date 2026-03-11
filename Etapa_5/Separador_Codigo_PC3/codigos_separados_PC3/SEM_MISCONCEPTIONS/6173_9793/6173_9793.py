opiniao = input('opiniao: ')

cont = 0
opiniao = opiniao.upper()

while opiniao != 'S':
	if opiniao == 'SIM':
		cont = cont + 1
	opiniao = input('opiniao: ')

print(cont)