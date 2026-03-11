a = float(input("informe o valor do patrimonio do banco Probresco: "))
b = float(input("informe o valor do patrimonio do anco bitcoin: "))
pa = float(input("informe o crescimento do banco Probresco: "))
pb = float(input("iforme o crescimento do banco bitcoin: "))
pA=(pa/100)+1
pB=(pb/100)+1
y=1

while(b < a):
	a=a*pA
	b=b*pB
	y=y+1
print(round(y,10))