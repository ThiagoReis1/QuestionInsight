compras = float(input())
opcaoPagamento = input().upper()

if(opcaoPagamento == 'D' or opcaoPagamento == 'P'):
	compras -= compras * 0.12
elif(opcaoPagamento == 'C2'):
	compras += compras * 0.07
	
print(round(compras,2))
