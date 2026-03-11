conta= float(input("digite o valor da conta:"))
#se o valor for menor ou igual 300
gorjeta= (10/100)*conta
#se o valor for superior a 300
gorjeta1= (6/100)*conta
if(conta<=300.0):
	pagar= gorjeta+conta
else:
	pagar= gorjeta1+conta
print(round(pagar, 2))