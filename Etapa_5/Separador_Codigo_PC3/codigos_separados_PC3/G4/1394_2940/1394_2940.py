## entrada
hr = float(input('Informe a quantidade de horas: '))

## condicionais
# pagamento = pg
## total de horas = hr
## hr = x + 20
x = hr - 20

if(hr <= 20):
	pg = 50 * hr
else:
	pg = ((50 * 20) + (70 * x))
print(round(pg, 2))
