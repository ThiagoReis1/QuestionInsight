x = float(input())
plano = (x*0.97)+45.00
icms = plano*42/100
total = plano+icms
print(round(total,2))