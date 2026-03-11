from numpy import *

horas = float(input("Digite as horas trabalhadas. "))

calc1 = horas*80+800
calc2 = horas*70+700
calc3 = horas*60+600
calc4 = horas*50+500

if(horas >= 30):
	print(round(calc1, 2))
elif(20 <= horas <30):
	print(round(calc2, 2))
elif(10 <= horas <20):
	print(round(calc3, 2))
elif(0 <= horas <10):
	print(round(calc4, 2))