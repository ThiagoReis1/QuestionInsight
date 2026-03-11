m= 0.28
f= 23

c= float(input("quantidade de chamadas em minutos: "))


v= (f+ c*m) + 31/100*(f+c*m)

print(round(v, 2))

