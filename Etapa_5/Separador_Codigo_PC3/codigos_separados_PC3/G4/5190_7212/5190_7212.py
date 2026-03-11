cc= int(input())
sn= float(input())

if(cc==101):
	s= sn+(sn*0.1)
	print(round(s,2))
	print("Aumento de 10 por cento")
else:
	s= sn+(sn*0.3)
	print(round(s,2))
	print("Aumenro de 30 por cento")