from numpy import*
v=array(eval(input("notas")))

m=(sum(v)-min(v))/ (size(v)-1)
print(round(m,2))
