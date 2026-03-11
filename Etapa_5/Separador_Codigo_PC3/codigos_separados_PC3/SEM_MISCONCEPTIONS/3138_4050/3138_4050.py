from numpy import *
v1 = array(eval(input("Digite o numero: ")))
media = ((v1[0])**7) + ((v1[1])**7) + ((v1[2])**7) + ((v1[3])**7) + ((v1[size(v1) - 1])**7)
m = (media/size(v1))**(1/7)

print(round(m, 2))