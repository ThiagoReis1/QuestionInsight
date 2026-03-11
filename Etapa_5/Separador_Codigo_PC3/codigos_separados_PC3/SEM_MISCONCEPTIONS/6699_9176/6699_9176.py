horas = float(input("Digite a quantidade de horas: "))
taxa_hora = horas * 15
taxa_fixa = 5
total = taxa_hora + taxa_fixa
icms = total * (20/100)
total = total + icms
print(round(total, 2))