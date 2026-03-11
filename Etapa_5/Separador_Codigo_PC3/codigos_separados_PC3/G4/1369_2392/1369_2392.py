# Leitura de quantidades de ingredientes
ruby = float(input())
gem = float(input())
dwarven = float(input())

# Quantidade de ingredientes necessários
flawless = 4.0
soul = 3.14
oleo = 10.0

#Calculo
A = (ruby / flawless)
B = (gem / soul)
C = (dwarven / oleo)

# Calculo de min
D = min(A, B, C)


# Saída de um número inteiro
print(int(D))