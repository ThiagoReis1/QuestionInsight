qh = float(input("quant de horas: "))
if 0 <= qh <= 10:
	vl = 50
	bn = 500
elif 10 <= qh <= 20:
	vl = 60 
	bn = 600
elif 20 <= qh <= 30:
	vl = 70
	bn = 700
elif 30 <= qh <= 9999999999999999999999:
	vl = 80
	bn = 800
	
pg = qh * vl + bn
print(pg)