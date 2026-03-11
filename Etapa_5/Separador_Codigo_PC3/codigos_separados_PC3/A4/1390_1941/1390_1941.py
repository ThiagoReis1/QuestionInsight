#franquia = 100 minutos
#qual o valor da conta?
min = int(input("digite o consumo de minutos: "))
if (min <= 100):
	conta = 1.20 * min
else:
	conta = 1.40 * min + 25
print (float(conta))