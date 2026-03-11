casca = float(input("quantidade de casca de colmeia: "))
alho = float(input("quantidade de alho: "))
oleot = float(input("quantidade de oleo de troll: "))

cas = casca // 0.2
alh = alho // 0.32
ole = oleot // 1.29

antidoto = min(cas, alh, ole) 

print(antidoto)