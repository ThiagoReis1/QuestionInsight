P = float(input("Digite o preco: "))
C = int(input("Digite o codigo da regiao (1,2,3,4): "))
D = 40/100
if(C==1):
	venda = (P-(P*D)+P*(10/100))
	print(round(venda,2))
elif(C==2):
	venda = (P-(P*D)+P*(8/100))
	print(round(venda,2))
elif(C==3):
	venda = (P-(P*D)+P*(0/100))
	print(round(venda,2))
elif(C==4):
	venda = (P-(P*D)+P*(2/100))
	print(round(venda,2))