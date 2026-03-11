vt = 1
pulv = 1
pilot = 1

tempo = int(input("tempo de voo: "))

if tempo < 0 and tempo <= 100:
	pulv = 80
	pilot = 3000
	vt = tempo * pulv * pilot
	print(vt)
elif tempo < 100 and tempo >= 200:
	pulv = pulv + 20
	pilot = pilot + 2000
	vt = tempo * pulv * pilot
	print(vt)