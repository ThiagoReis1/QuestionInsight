qcc = float(input("Quantidade de casca de colmeia: "))
qa = float(input("Quantidade de casca de alho: "))
qot = float(input("Quantidade de casca de Óleo de Troll: "))

dcc = (qcc / 0.2)
da = (qa / 0.32)
dot = (qot / 1.29)

ant = min(dcc, da, dot)

print(int(ant))