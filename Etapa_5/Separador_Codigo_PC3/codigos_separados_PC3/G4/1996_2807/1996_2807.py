ami = input("")
a = ami.lower()

O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.0079

if(a == "aspartato"):
	x = (C*4)+(H*6)+N+(O*4)
	print (round(x, 2))
elif(a == "fenilalanina"):
	x = (C*9)+(H*11)+(O*2)+S
	print (round(x, 2))
elif (a == "tirosina"):
	x = (C*9)+(H*11)+N+(O*3)
	print (round(x, 2))
else:
	print("Entrada:", ami)
	print("Dado Invalido")