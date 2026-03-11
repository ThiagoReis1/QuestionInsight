from numpy import*

v = array(eval(input()))
p = ([1, 3, 2, 5])

s = v * p
m = sum(s) / sum(p)

print(round(m, 2))
