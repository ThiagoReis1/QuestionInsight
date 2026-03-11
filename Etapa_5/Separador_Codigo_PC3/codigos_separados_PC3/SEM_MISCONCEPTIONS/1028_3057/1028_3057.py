#ENTRADA
consumo = float (input ("informe o valor consumido: "))


soma = (consumo * 0.37 ) + 15
icms = soma * 35/100
total = soma + icms


print (round (total , 2))