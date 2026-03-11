qh = float(input(" "))
if (qh <= 20):
	sala = (qh * 50)
	print(round(sala,2))
else:
	sala = (20 * 50) + (qh - 20) * 70
	print(round(sala,2))