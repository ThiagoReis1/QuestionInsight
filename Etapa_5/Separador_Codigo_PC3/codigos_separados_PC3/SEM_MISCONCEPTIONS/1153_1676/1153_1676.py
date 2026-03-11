Naprox = int(input("No. de aproximacoes: "))
cont = 0
sinal = 1
while (cont < Naprox):
 # Computa novo termo da serie do PI
 PIaprox = PIaprox + sinal * 4. / (2*cont + 1)
 # Atualiza sinal do proximo termo
 sinal = - sinal
 # Incrementa contador
 cont = cont + 1

# Imprime resultado
print(round(PIaprox, 8))