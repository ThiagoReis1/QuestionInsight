compra=float(input())
codigo= input()
if codigo=='D':
	total=(compra-(compra*0.19))
elif codigo=='P':
	total=(compra-(compra*0.19))
elif codigo=='C':
	cartao=input()
	if cartao=='1':
		total=compra
	else:
		total= (compra+(compra*0.09))
print(round(total,2))