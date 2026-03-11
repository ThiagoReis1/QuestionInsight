consumo = float(input(" digite o valor consumido no mes: "))
acrescimo = consumo * 0.28 + 23.0
icms = acrescimo * (31/100) 
total = acrescimo + icms
print (round(total,2))
