from numpy import*

v0 = array([3,2,4,1,3])
v1 = array(eval(input()))

mul = v0 * v1
soma = sum(mul)
media = soma / sum(v0)

print(round(media,2))