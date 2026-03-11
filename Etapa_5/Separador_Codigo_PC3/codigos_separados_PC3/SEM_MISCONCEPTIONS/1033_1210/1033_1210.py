# Universidade Federal do Amazonas
# Aluno: Philippe da Silva Soares
# Matrícula: 21650892
# Objetivo:

# Peso da mercadoria
peso=float(input("informe o peso da mercadoria: "))

custo_por_kg=43.21
taxa_aero=25.00
ICMS=(peso*custo_por_kg+taxa_aero)*0.62

# Valor total a ser pago
valor_total=(peso*custo_por_kg+taxa_aero+ICMS)

print(round(valor_total,2))

