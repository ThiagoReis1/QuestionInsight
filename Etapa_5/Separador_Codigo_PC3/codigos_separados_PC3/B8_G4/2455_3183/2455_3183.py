exp = int(input("nivel de experiencia "))
qta = float(input("quantidade de horas "))

if(exp == 1):
	sal = (qta * 12.00)
elif(exp == 2):
	sal = (qta * 17.00)
elif(exp == 3):
	sal = (qta * 25.00)
	
print(round(sal , 2))