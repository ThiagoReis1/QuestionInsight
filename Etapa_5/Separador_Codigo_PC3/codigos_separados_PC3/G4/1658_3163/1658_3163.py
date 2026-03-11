from numpy import *

n = input("Informe a etnia: ")

vetor = []

g = n.split(',')

b = g.count('CHN')
pa = g.count('JPN')
pr = g.count('KOR')
a = g.count('MGL')
i = g.count('THA')

vetor.append(b)
vetor.append(pa)
vetor.append(pr)
vetor.append(a)
vetor.append(i)

print(max(vetor))
print(array(vetor))