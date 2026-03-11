from math import* 
m= float(input("Digite o valor da mensalidade, em R$: "))
c= int(input("Digite a quantidade de criancas na familia: "))

if(c >= 3):
	V= (m*c)
	T=V-V*(40/100)
	print(round(T,2))
if(c == 2):
	V= (m*c)
	T= V-V*(30/100)
	print(round(T, 2))
elif(c==1):
	V =(m*c) 
	T =V- V*(10/100)
	print(round(T, 2))