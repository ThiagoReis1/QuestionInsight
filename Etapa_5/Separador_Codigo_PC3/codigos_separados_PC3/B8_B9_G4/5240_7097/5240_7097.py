c=int(input("qual o consumo da residencia?"))
ip=50
if c>0:
	if c<100:
		print(round(ip+c*0.5,2))
	elif c>=100 and c<250:
		print(round(ip+c*0.75,2))
	elif c>=250 and c<500:
		print(round(ip+c*1,2))
	elif c>=500:
		print(round(ip+c*1.25,2))
else:
	print("Dados invalidos")