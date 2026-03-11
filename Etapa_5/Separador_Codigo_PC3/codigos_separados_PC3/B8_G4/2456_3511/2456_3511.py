m = float(input("Valor da mensalidade: "))
c = float(input("Numero de criancas: "))
vt= m * c
if(c==1):
	print(round((vt * 10) / 100),2)
elif(c==2):	
	print(round((vt * 30) / 100),2)
elif(c>=3):
	print(round((vt * 40) / 100),2)