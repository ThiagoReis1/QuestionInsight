encomenda = float(input())
encomenda = round(encomenda,2)
imposto = (81 * encomenda)/100
imposto = round(imposto,2)
valor_pago = 12.0 + imposto + encomenda

print(round(valor_pago,2))