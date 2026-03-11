casca_colmeia = float(input("quantidade de casca de colmeia: "))
alho = float(input("quantidade de alho: "))
oleo_troll = float(input("quantidade de oleo de troll: "))

c_c = casca_colmeia//0.2
a = alho//0.32
o_t = oleo_troll//1.29

antidoto = int(min(c_c, a, o_t))

print(antidoto)