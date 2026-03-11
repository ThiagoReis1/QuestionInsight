#variaveis
vel = int ( input ("Velocidade da Internet: "))


#cond
if vel < 50:
	soma = 60.00 + 4.50
	print (round ( soma , 2 ))
elif vel == 50:
	soma = 60.00 + 5.50
	print (round ( soma , 2 ))
else:
	soma = 60.00 + 6.50
	print (round ( soma , 2 ))