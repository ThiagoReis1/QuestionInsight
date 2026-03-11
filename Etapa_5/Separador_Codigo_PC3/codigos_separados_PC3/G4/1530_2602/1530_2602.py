from math import*
p = int(input("Quantidade de pergaminhos: "))
v = int(input("Quantidade de varinhas: "))
cp = float(input("Percentual de crescimento pergaminhos: "))
cv = float(input("Percentual de crescimento varinhas: "))
anop = 0
anov = 0
armaz = 0
anos = 0
while (armaz <= 80000):
	anop = anop + (p * cp)/100
	anov = anov + (v * cv)/100
	armaz = anop + anov
	anos = anos + 1
print(anos)
	

