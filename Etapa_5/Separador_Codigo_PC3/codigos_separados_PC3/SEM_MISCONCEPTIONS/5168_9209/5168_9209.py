# peso do saco de racao
saco = float(input("Quantidade de racao em gramas no saco?: "))
# quantidade diaria de racao usada
diaria = float(input("Quantidade de racao diaria?: "))

sobra = saco - diaria*7 # sobra no saco em uma semana

print(round(sobra, 4)) # imprimindo a sobra