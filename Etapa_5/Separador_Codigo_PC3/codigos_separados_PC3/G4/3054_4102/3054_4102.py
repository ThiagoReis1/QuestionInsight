h = float(input("Quantidade de horas trabalhadas: "))
if (h>=0):
	if(0 <= h <= 10):
		print(round((h*50)+500, 2))
	elif(10 < h <= 20):
		print(round((h*60)+600, 2))
	elif(20 < h <= 30):
		print(round((h*70)+700, 2))
	else:
		print(round((h*80)+800, 2))