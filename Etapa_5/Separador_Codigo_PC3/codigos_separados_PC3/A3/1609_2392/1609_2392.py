from numpy import*
v1 = array(eval(input()))
palavra = input()
i = 0
while(palavra=="ARARA".replace("R","L")):
	v1 = v1 + v1[0]
	print(v1)