area = int(input(""))
#valor = area * custo + fert
if(area >= 0) and (area < 10000):
	print(area * 6 + 100)
elif(area >= 10000) and (area < 20000):
	print(area * 5.50 + 150)
elif(area >= 20000) and (area < 30000):
	print(area * 5 + 200)
elif(area >= 30000):
	print(area * 4.50 + 250)