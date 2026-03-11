from numpy import*
v=array(eval(input("vetor de notas: ")))
x=(sum(v)-min(v))/(size(v)-1)
print(round(x,2))