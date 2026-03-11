altm = 1.4
tm = 0.06

altl = float(input("Digite a altura de um leao: "))
tl = float(input("Digite a taxa de crescimento do leao: "))

anos = 0 #variavel conatdora dos anos

while(altl >= altm):
	altm = altm + tm
	altl = altl + tl
	anos = anos + 1
	
print(anos)