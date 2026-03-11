peso_saco = float(input())
qtd_diaria = float(input())

qtd_restante = peso_saco - (5 * qtd_diaria)
qtd_restante_at = round(qtd_restante, 2)

print(qtd_restante_at)