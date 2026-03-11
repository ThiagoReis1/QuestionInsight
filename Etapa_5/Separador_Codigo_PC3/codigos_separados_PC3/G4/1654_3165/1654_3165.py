from numpy import *

n = input(": ")

vetor = []

g = n.split(',')

b = g.count('AM')
pa = g.count('PE')
pr = g.count('MG')
a = g.count('SP')
i = g.count('RS')

vetor.append(b)
vetor.append(pa)
vetor.append(pr)
vetor.append(a)
vetor.append(i)

print(max(vetor))
print(array(vetor))