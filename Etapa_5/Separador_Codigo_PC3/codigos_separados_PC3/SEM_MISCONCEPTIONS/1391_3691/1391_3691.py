valor = float(input())
if valor <= 150 :
	conta = 0.6*valor + 5
else:
	conta= 0.75*valor + 16
print(round(conta,2))