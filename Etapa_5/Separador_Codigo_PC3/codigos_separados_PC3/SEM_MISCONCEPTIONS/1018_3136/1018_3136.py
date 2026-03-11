#entradas

primeiro_cateto = float(input("Comprimento 1 da fazenda: "))
segundo_cateto = float(input("Comprimento 2 da fazenda: "))
custo = float(input("Custo em m2: "))

#calculo

area = (primeiro_cateto * segundo_cateto) / 2

custo_total = (area * custo)

#resultado

print(round(custo_total, 2))

