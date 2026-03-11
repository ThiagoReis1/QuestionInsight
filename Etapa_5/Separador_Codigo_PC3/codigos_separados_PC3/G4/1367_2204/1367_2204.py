a = float(input("quantidade de snowberry : "))
b = float(input("quantidade de sais de fogo : "))
c = float(input("quantidade de amanita : "))
snow = 0.31
sais = 0.73
amanita = 2.64
x = a // snow
y = b // sais
z = c // amanita 
print(int(min(x,y,z)))
		