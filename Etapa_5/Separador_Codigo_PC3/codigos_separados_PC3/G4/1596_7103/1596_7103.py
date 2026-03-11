from numpy import*
notas = array(eval(input("Notas: ")))

n = sum(notas) - min(notas)
p = size(notas) - 1
c = n/p
print(round(c,2))




	