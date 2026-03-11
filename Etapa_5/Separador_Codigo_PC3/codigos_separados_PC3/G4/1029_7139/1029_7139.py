# Entrada

CS = float(input("Minutos consumidos:"))

# Calculo

V = (0.28 * CS + 23.0)
I = (V * 0.31)
T = (V+I)
#Saida

print(round(T,2))