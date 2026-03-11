from numpy import*
v=array(eval(input("v:")))
i=0
s=(sum(v)-min(v))/(size(v)-1)
print(round(s,2))
