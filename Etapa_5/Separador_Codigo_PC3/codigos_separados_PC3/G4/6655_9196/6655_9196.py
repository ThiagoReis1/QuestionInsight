from numpy import*
v= array(eval(input("notas:")))
p = [5,1]
k = sum(p)
s = ((p[0]*v[0])+ (v[1]* p[1]))/k
print(round(s,2))