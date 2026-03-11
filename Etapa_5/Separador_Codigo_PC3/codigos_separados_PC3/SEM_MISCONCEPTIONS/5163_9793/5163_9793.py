peso = float(input("insira o peso do saco de racao de cleosmeria em gramas: "))
diaria = float(input("Quantos gramas o gato precisara comer diariamente: "))

rest = peso - (5 * diaria)

print(round(rest, 3))
