dano = int(input())
forca = int(input())
recuperada = int(input())

r= forca

while( r > 0):
	r= r - dano * 5 + recuperada


print(r)