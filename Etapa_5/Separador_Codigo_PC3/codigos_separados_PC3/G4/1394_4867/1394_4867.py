hr=float(input("Horas trabalhadas?"))
if(hr<=20):
	pg=hr*50
else:
	aux=hr-20
	pg=(20*50)+(aux*70)
print(round(pg,2))