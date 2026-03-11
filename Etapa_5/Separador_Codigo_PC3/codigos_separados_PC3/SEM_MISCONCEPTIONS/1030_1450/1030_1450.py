# Universidade Federal do Amazonas
# Aluna: Karina Rocha Ferreira - 21554907
# Avaliacao 1 - 15/06/2015

qtd_exc = float(input())

plano = 45.00
exc = 0.97
total = plano + (exc * qtd_exc)
imposto = total * 42 / 100
pago = total + imposto

print(round(pago,2))