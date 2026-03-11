pc = float(input("Digite o custo: "))

if(pc < 50.0):
	soma = pc * 2
	print(soma)
elif( pc > 50.01 or pc < 100.00):
	soma = pc + (pc * 1/2)
	print(round(soma,2))
elif(pc > 100.01 or pc < 500.00):
	soma = pc + (pc * 0.40)
	print(round(soma,2))
else:
	soma = pc + (30/100)
	print(round(soma,2))