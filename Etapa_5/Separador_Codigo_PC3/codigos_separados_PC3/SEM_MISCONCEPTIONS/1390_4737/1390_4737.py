consumo=float(input("Minutos Consumidos: "))
if(consumo<=100):
	valor=(consumo*1.2)
	conta=valor
else:
	valor_ex=consumo*1.4
	ttl=25+valor_ex
	conta=ttl
print(round(conta,2))