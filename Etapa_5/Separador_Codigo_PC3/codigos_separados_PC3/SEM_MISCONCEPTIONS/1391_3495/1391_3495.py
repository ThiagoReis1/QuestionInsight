consumo=float(input())

if(consumo<=150):
	total=(consumo*0.60)+5
	print(round(total,2))
else:
	total=(consumo*0.75)+16
	print(round(total,2))