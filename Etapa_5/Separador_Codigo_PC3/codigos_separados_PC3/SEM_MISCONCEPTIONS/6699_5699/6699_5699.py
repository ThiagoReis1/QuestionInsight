tempo = int(input())

icms = (tempo*15 + 5)*0.2
valor_total = tempo*15 + 5 + icms

print(round(valor_total,2))