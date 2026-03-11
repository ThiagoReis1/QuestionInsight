ch=float(input('Carga horaria: '))

if(ch<=10):
	p=ch*50+500
elif(10<ch<=20):
	p=ch*60+600
elif(20<ch<=30):
	p=ch*70+700
elif(30<ch):
	p=ch*80+800
print(round(p,2))