qh = float(input("quantidade de horas: "))

if qh<=20:
	x= qh * 50.00

else:
	s = (20*50)
	r = (qh-20)
	x = s + (r*70)
print(round(x,2))