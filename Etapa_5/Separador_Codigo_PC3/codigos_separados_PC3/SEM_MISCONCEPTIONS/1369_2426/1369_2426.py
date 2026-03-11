chif = 4.0
our = 3.14
ole = 10.0

chifre  = float(input("Chifre de ouro: "))
ouro = float(input("Ouro em pó: "))
oleo = float(input("Óleo de dwarven: "))

# Uma poçao tem:
pchifre = chifre // chif #pode fazer x porçoes
pouro = ouro // our #pode fazer x porçoes
poleo = oleo // ole #pode fazer x porçoes

print(int(min(pchifre, pouro, poleo)))