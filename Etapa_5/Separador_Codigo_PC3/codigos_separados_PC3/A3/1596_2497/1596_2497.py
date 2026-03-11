from numpy import*
v = array(eval(input("vetor: ")))
menorn = min(v)
nota = sum(v) - min(v)
print(round(nota/(size(v)-1) ,2))
#print(round(sum(v)/size(v),2))

