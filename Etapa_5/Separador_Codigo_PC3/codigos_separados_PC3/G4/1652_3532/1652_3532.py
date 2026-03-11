from numpy import *

n = input("Informe a etnia: ")

vetor = []

g = n.split(',')

b = g.count('B')
pa = g.count('PA')
pr = g.count('PR')
a = g.count('A')
i = g.count('I')

vetor.append(b)
vetor.append(pa)
vetor.append(pr)
vetor.append(a)
vetor.append(i)

print(max(vetor))
print(array(vetor))