import math


def arco_flecha(ang, v0):
	G = 9.8
	return pow(v0,2)* (math.sin(2*ang)) / G


if __name__ == '__main__':
	ang = math.radians(float(input("Digite o angulo: ")))
	v0 = float(input("Digite a vel. inicial: "))
	print(round(arco_flecha(ang, v0),2))