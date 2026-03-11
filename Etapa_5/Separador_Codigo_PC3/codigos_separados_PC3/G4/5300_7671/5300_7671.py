#Piao

velo = float(input("Qual a velocidade de rotacao inicial? "))

while(velo >= 50):
	print(round(velo,2))
	velo = velo - velo * 25/100
	