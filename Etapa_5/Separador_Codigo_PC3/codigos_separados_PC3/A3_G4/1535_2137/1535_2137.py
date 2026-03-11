x = float(input("digite aqui: "))
k = int(input("Digite aqui: "))
t=0
x=1
while(t<k):
	arctg = x + ((-1)**(2*t + 1))*x**(2*t+1)/(2*t+1) 
	t=t+1
print(round(x,6))	
	