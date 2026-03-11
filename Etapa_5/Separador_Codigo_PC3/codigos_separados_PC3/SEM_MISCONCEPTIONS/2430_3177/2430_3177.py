capital = float(input("valor total"))
tempo = float(input("quantidade"))
tj = 3/100
J = (capital * (tj * tempo))/100
M = capital + J
print(round(M,2))