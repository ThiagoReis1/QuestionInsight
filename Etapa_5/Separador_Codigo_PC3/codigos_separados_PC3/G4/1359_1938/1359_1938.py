from math import*
ve = float(input("velocidade de exaustao: "))
mo = float(input("massa inicial : "))
mf = float(input("massa final : "))
detav = ve*log(mo/mf)
print(round(detav,2))