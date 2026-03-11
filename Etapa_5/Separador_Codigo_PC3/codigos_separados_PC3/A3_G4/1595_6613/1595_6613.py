from numpy import*
v = array(eval(input("Notas: ")))

a= min(v)
b = sum(v)-min(v)
c= size(v)-1

d=b/c

#print(a)
#print(b)
#print(c)
print(round(d,2))