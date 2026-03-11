custo= float(input())
if 0<custo<= 50:
	ts= custo * (100/100)
	tt= custo + ts
	print(round(tt,2))
elif 50.01<= custo<= 100:
	ts= custo * (50/100)
	tt= custo +ts
	print(round(tt,2))
elif 100.01 <= custo <= 500:
	ts= custo * (40/100)
	tt = custo + ts
	print(round(tt,2))
elif custo >= 500:
	ts= custo * (30/100)
	tt= custo + ts
	print(round(tt,2))