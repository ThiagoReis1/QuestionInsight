valor=float(input("Digite um valor: "))

if (valor<=1000):
	msg= valor+((valor*5)/100)
else:
	V1=(valor-1000)+((valor-1000)*(5/100))
	V2=valor+((valor*10)/100)
	msg=V2-V1
print(round(msg, 2))