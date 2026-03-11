a = float(input("valor_da_mensalidade: "))
b = int(input("criancas: "))
if(b==1):
	v = ((a*b)*10/100)
	c = (a*b)-v
	print(round(c,2))
elif(b==2):
	v = ((a*b)*30/100)
	c = (a*b)-v
	print(round(c,2))
elif(b>=3):
	v = ((a*b)*40/100)
	c = (a*b)-v
	print(round(c,2))
	