from numpy import*
v = array(eval(input("vetor: ")))
media_ponderada = ((v[0]*2) + (v[1]*2) + (v[2]*6) + v[3])/11
print(round(media_ponderada,2))