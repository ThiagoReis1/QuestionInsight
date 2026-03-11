#entradas 

qtd = float(input("chamadas: "))

porcentagem = 31 / 100
total = (qtd * 0.28) + 23
acrescimo = total * (porcentagem)
valor = total + acrescimo

print(float(round(valor, 2)))