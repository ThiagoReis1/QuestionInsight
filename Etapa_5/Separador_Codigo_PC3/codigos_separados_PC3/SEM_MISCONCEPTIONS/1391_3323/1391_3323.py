#varavel=tipo(input("mensagem: "))  //tipo(int, float)
consumo=int(input("consumo"))

x=(consumo*0.60)+5
y=(consumo*0.75)+16

if(consumo<=150):
	print(round(x,2))
	
else:
	print(round(y,2))
	
