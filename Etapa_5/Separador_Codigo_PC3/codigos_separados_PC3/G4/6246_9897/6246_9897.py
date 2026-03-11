time = input('time: ').upper()

cont = 0 #qntd respostas

while time != 'X':
	if time == 'A':
		cont += 1
	time = input('time: ')
print(cont)