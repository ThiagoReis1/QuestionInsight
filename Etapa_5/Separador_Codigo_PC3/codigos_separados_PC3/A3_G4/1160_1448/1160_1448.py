H = int( input("digite o numero de Habitantes:")) 
V = int( input("numero de vampiros:"))
X = int( input("pessoas transformadas em vampiros por dia:"))
Y = int( input("grupo de cacadores:"))

i = 0
while (i <= H):
	transformadas = (V * X)
	dias = transformadas * Y
	i = i + X
print ("quantidades de dias em que as pessoas serao transformadas:", transformadas)