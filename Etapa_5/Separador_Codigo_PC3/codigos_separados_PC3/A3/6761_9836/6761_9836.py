# faça seu código aqui!
mes=60
taxa1=4,50
taxa2=5,50
taxa3=6,50

vel=int(input('velocidade:'))


if (vel < 50):
	total=60+4.50
elif (vel == 50 ):
	total=60+5.50
else:
	total=60+6.50
	
print(round(total,1))