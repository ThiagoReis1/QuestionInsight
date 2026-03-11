#onpprod
time = float(input("Tempo de voo:"))
if(time<=200):
	custo = 5000.0+100.0*time
	print(round(custo,2))
else:
	custo = (8000.0)+(200*100)+(90*(time-200))
	print(round(custo,2))