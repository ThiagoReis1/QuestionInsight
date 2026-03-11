a = float(input("valor da mensalidade"))
b = int(input("numero de criancas"))

if(b==1):
	x = a*b-(a*b*0.1)
elif(b==2):
	x = a*b-(a*b*0.3)
elif(b>=3):
	x = a*b-(a*b*0.4)

print(round(x,2))