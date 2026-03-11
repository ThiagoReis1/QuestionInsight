mercadoria = float (input ("Digite o peso da mercadoria a ser transportada: "))

frete = (mercadoria * 43.21) + 25
imposto = (62/100) * frete

valortotal = frete + imposto

print (round(valortotal, 2))