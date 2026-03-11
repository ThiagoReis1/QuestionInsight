#Conta de Celular

plano = 45.00
juros = 0.97
minutos = 60

x = float(input("Quantos minutos voce excedeu? "))

valor = x*juros
soma = valor+plano
imposto = soma*0.42
total = soma + imposto

print (round(total,2))
