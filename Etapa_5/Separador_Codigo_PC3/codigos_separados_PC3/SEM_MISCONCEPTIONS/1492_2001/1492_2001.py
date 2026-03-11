from math import *

horas = float(input("Digite a carga horaria: "))

if (0 < horas < 10):
	bon =  horas * 50 + 500
	print(round(bon,2))
elif (10 <= horas < 20):
	bon =  horas * 60 + 600
	print(round(bon,2))
elif (20 <= horas < 30):
	bon =  horas * 70 + 700
	print(round(bon,2))
elif (horas >= 30):
	bon =  horas * 80 + 800
	print(round(bon,2))
else: 
	print()

