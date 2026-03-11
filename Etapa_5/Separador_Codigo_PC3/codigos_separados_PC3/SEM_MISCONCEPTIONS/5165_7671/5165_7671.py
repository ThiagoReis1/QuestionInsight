# Cleo

peso = float(input("Qual o peso do saco de racao?"))

quantidade_diaria = float(input("Quantas gramas de racao e consumida diariamente?"))

seis_dias = quantidade_diaria * 6

resto = peso - seis_dias

print(round(resto, 4))