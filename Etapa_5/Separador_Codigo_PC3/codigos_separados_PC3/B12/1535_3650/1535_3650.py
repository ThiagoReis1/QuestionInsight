x= float(input(' insira um numero inteiro '))
termo = int(input(' insira o numero de termos '))
y = 1
arctg = 0
while termo>0 and (x>=-1 or x<=1):
	if termo>0:
		arctg = arctg + (x**y/y) 
		termo = termo-1
		y = y+2
	if termo>0:
		arctg = arctg - (x**y/y)
		termo = termo-1
		y = y+2
print(round(arctg,6))
		
	