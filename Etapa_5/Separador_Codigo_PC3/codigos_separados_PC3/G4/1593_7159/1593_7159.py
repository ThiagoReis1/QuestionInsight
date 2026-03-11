from numpy import*

notas = array(eval(input("notas: ")))

v = arange(size(notas) + 1)
a = v[1:]
y = notas * a
g = sum(y)/sum(a)

print(round(g,2))