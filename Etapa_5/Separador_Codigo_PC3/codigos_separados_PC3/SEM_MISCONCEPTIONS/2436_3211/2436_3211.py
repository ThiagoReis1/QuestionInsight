peso = float(input())
distancia = float(input())
valor_primario = peso*25 + distancia*0.10
ICMS = 0.12*valor_primario
valor_final = valor_primario + ICMS

print(round(valor_final, 2))