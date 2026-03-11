from numpy import *

n = input("Informe os paises de origem: ")

x = []

g = n.split(',')

be = g.count('BE')
es = g.count('ES')
fr = g.count('FR')
it = g.count('IT')
pt = g.count('PT')

x.append(be)
x.append(es)
x.append(fr)
x.append(it)
x.append(pt)

print(max(x))
print(array(x))