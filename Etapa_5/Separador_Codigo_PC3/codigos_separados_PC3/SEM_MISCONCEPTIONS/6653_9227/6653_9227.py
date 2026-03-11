from numpy import*

v = array(eval(input("")))

p = [3,5,1]

total = (v[0]*p[0] + v[1]*p[1] + v[2]*p[2])/sum(p)

print(round(total, 2))

