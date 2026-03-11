x= float(input("Digite o valor de x: "))
if x>=-100 and x<0:
	print(round((-1/x),4))
elif x >0 and x<=100:
	print(round(1/x,4))
else:
	print("entrada invalida")