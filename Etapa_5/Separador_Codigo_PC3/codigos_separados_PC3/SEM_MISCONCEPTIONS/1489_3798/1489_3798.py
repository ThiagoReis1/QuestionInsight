consumo=float(input("consumo:"))
if(consumo>=0) and (consumo<=150):
	valor=(consumo*0.60)+5.00
elif(consumo>=150) and (consumo<=250):
	valor=(consumo*0.65)+8.00
elif(consumo>=250) and (consumo<=350):
	valor=(consumo*0.70)+12.00
else:
	valor=(consumo*0.75)+16.00
print(round(valor,2))