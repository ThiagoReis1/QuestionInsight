from math import*

# Ler as entradas 1- estimativas de açai por metro quadrado ; 2- O comprimento da aresta  

est_acai = float(input("Digite a estimativa de acaizeiros: "))
com_aresta = float(input("Digite a comprimento da aresta em metros: "))

# Calcular 

area = 3 * (sqrt( 3 * com_aresta **2)/2)
total = area * est_acai

# Print da quantidade total de açai

print(int(total))