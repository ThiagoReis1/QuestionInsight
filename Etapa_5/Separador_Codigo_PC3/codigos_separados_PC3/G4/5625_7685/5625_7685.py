k= input("tapioca(T) ou salgado(S): ")
q= int(input("quantidade d tapioca ou salgado: "))
a= int( input("quantidade de acai: "))

if(k.upper()=="T"):
	v=q*5.50+a*10.00
	print(round(v, 2))
else:
	v=q*4.00+a*10.00
	print(round(v, 2))