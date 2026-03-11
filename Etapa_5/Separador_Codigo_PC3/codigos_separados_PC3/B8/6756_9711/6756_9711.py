# faça seu código aqui!
quant = int(input())
diaria = 175
if quant < 15:
	soma = quant * diaria + 20 
elif quant == 15:
	soma = quant * diaria + 16
elif quant > 15:
	soma = quant * diaria + 10
print(round(soma, 2))
	