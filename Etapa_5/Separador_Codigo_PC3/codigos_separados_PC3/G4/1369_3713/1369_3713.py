chifre = float(input()) 
ouro = float(input())
gramas = float(input())
c= 4
o= 3.14
oleo = 10

q_ch = chifre/c
our = ouro / o
g = gramas / oleo

v = min(q_ch, our, g)

print(int(v))
