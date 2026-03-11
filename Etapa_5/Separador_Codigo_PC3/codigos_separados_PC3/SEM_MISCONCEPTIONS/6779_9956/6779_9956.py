nasc = int (input("data de nascimento"))
op = input("pais").upper()

cal = 2023 - nasc

if op=='B':
	if cal > 18:
		print(sim)
		print(round(cal-18))
	elif cal<18:
		print(nao)
		print(round (18 - cal))
if op == 'J':
	if cal > 16:
		print (sim)
		print (round(cal-16))
		elif cal < 16:
			print (nao)
			print(roud(16-cal))

	
	
	

	
	
	





