peso = float(input('Peso da mercadoria em quilo:'))
custo = (peso*43.21)+25
imposto = custo*0.62
total = (custo+imposto)
print(round(total, 1))