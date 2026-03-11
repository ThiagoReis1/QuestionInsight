from numpy import*

v = array(eval(input("vetor string: ")))
vi = array(eval(input("vetor inteiro: ")))

GELO = 2
FOGO = 3
CHOQUE = 4
CONJURACAO = 8
ILUSAO = 10


d1 = v[0] * vi[0]
d2 = v[1] * vi[1]
d3 = v[2] * vi[2]
d4 = v[3] * vi[3]

dt = d1 + d2 + d3 + d4

print(dt)