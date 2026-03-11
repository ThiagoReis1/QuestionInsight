tempo_de_estacionamento = float(input("Digite o tempo de estacionamento (em Horas): "))

taxas_padrao = 15 * tempo_de_estacionamento + 5

resultado_1 = taxas_padrao * (20 / 100)

resultado_total = taxas_padrao + resultado_1

print(round(resultado_total, 2))