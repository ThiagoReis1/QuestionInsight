t = float(input("Digite o tempo necessario: "))
me = t-200
if (t<=200):
	p = 5000+100*t
	
else:
	p = 8000+100*200+90*me

print(round(p,2))