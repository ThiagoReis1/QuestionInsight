h = int(input("quantidade de habitantes: "))
v = int(input("quantidade de vampiros: "))
x = int(input("quantidade de transformacoes: "))
y = int(input("quantidade de vampiros mortos: "))
dia = 0
while(h > 2):
	v = v * x
	v = v - y
	h = h - v
	dia = dia + 1
print(dia)