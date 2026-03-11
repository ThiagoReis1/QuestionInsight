horas= float(input("quantidade de horas trabalhadas:"))
if (horas <= 20):
	total = horas * 50
	print (total)
else:
	total = (20*50)+ ((horas-20)*70)
	print (total)