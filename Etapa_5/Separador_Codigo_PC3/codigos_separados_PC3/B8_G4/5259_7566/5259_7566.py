x = float(input("insira o valor da mensalidade: "))
y = int(input("insira a quantidade de criancas: "))
if(y == 1):
	a = y*x - y*x*0.10
elif( y == 2):
	a = y*x - y*x*0.3
elif(y>=3):
	a = y*x - y*x*0.40
print(round(a, 2))