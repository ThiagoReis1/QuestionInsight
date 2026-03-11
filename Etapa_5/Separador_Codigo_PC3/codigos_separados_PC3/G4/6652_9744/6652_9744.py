from numpy import*
v = array(eval(input()))
v1 = [2, 2, 6, 1]
v2 = v*v1
soma = sum(v1)
soma1 = sum(v2)
r = soma1/soma
print(round(r, 2))