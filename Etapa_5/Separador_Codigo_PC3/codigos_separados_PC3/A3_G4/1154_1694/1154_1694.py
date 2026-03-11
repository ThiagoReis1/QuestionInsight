hiv=float(input("Num inicial:"))
taxa=float(input("Taxa redução:"))
num=float(input("Num copias/semana:"))

taxap=taxa/100
#acumuladora HIV/semana
virus=hiv
#contadora semana
s=0

while virus<1000000:
	dim=(virus*taxa)
	res=num-dim
	virus=virus+res
	s=s+1
print(s+1)