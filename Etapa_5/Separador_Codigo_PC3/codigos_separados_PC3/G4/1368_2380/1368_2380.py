#0.2 g casca de colmeia#
#0.32 g gramas de alho#
#1.29 g de óleo de troll#
gc=float(input())
ga=float(input())
go=float(input())
qmo=int(go/1.29)
qma=int(ga/0.32)
qmc=int(gc/0.2)
print(min(qmo,qma,qmc))
