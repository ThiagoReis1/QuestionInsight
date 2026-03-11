x = float(input('digite o valor:'))
k = int(input('digite o valor:'))
i = 1
arct = 1

while(x<k):
	arct = arct + (-x)**(2*i+1)/(2*i+1)
	i = i + 1
print(round(artc,6))
