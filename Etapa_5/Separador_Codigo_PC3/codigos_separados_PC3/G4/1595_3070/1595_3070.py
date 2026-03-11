from numpy import*
v = array(eval(input("vetor de notas: ")))

n = (sum(v) - min(v))/(size(v) - 1)


print(round(n, 2))