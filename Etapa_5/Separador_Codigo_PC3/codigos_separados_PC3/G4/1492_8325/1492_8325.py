h=float(input("horas trabalhadas: "))

if(h>=0 and h<=10):
	p=h*50+500
	print(round(p,2))
elif(h>10 and h<=20):
	p=h*60+600
	print(round(p,2))
elif(h>20 and h<=30):
	p=h*70+700
	print(round(p,2))
else:
	p=h*80+800
	print(round(p,2))