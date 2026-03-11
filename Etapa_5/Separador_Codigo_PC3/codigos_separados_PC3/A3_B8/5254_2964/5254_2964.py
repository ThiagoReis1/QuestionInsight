preco = float(input())
cod = int(input())
frete = 0

if(cod == 1):
	frete = 0.1
elif(cod == 2):
	frete = 0.08
elif(cod == 4):
	frete = 0.02
	
print(round(((preco * 0.6) + (preco * frete)), 2))