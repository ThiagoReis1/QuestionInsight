from numpy import *
n = input("Informe a string correspondete as cores dos olhos: ")

ar = []

g = n.split(',')

count_p = g.count('P')
count_c = g.count('C')
count_m = g.count('M')
count_v = g.count('V')
count_a = g.count('A')

ar.append(count_p)
ar.append(count_c)
ar.append(count_m)
ar.append(count_v)
ar.append(count_a)

print(max(ar))
print(array(ar))





