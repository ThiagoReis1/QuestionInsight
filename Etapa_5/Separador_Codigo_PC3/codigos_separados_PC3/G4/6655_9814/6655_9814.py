from numpy import * 

vp = array([5, 1])
vn = array(eval(input('determine o vetor notas: ')), dtype=int)

mp = round((sum(vp * vn) / sum(vp)), 2)

print(mp)