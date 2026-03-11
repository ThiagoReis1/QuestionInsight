from numpy import*
v = array(eval(input("notas ")))
t1 = v[0]
t2 = v[1]*2
t3 = v[-1]*3
m = (t1 + t2 + t3)/size(v)
print(round(m, 2))