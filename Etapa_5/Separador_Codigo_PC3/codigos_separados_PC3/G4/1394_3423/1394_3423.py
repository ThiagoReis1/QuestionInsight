h= float(input("horas trabalhadas: "))
a= h*50
b= ( a + (h-20)*20) 
if (h <= 20):
	print(round(a,2))
else:
	print(round(b,2))