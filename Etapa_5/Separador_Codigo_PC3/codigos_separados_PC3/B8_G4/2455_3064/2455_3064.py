x=int(input("Informe o nivel de experiencia do professor: "))
y= float(input("Horas de trabalhos que o professor execulta: "))
if (x==1):
	print(round(y*12,2))
elif (x==2):
	print(round(y*17,2))
elif (x==3):
	print(round(y*25,2))	