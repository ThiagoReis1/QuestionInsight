energia=float(input("consumo de energia kWh: "))
if(energia>=0 and energia<=150):
	valor=(energia*0.60)+5
	print(round(valor,2))
elif(energia>150 and energia<=250):
	valor=(energia*0.65)+8
	print(round(valor,2))
elif(energia>250 and energia<=350):
	valor=(energia*0.70)+12
	print(round(valor,2))
elif(energia>350):
	valor=(energia*0.75)+16
	print(round(valor,2))