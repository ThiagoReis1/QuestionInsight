vel = int(input('escolha a velocidade de sua internet:'))

if vel < 50:
	internet = 60.0 + 4.50
	print(round(internet, 1))
	
elif vel == 50:
	internet = 60.0 + 5.50
	print(round(internet, 1))
	
elif vel > 50:
	internet = 60.0 + 6.50
	print(round(internet, 1))
	