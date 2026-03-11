di = int(input())
meses = int(input())

juros = 0.01
soma = 0 


while (meses >= 0):
	soma = di + (juros)*di
	print(round(soma,2))
	
	
	
