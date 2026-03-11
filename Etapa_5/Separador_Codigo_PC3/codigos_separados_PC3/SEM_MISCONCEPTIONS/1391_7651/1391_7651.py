consumo = float(input())

if(consumo <= 150):
	a = (consumo * 0.60)+5
	print(round(a, 2))
else:
	ab = (consumo * 0.75)+16
	print(round(ab, 2))