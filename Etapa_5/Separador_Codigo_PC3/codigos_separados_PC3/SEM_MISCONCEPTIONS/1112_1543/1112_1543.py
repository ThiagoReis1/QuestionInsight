x = float(input("Digite o valor salarial: "))

if((x<800) and (x>0)):
	print(round,x,2)
	Novosalario = (x*100/50)
elif(x>800<=1000):
	print(round,x,2)
	Novosalario = (x*100/40)
elif(x>1000<1200):
	print(round,x,2)
	Novosalario = (x*100/30)
elif(x>1200<1400):
	print(round,x,2)
	Novosalario = (x*100/20)
elif(x>1400<1600):
	print(round,x,2)
	Novosalario = (x*100/10)
elif(x>1600):
	print(round,x,2)
	Novosalario = (x*100/5)
	print(round,Novosalario,2)
else:
	print("Dado invalido")