temp = float(input("Digite o tempo: "))
if(temp<=200):
	cust = 5000+(temp*100)
	print(round(cust,2))
else:
	ex = temp - 200
	cust = 8000+(200*100)+(90*ex)
	print(round(cust,2))