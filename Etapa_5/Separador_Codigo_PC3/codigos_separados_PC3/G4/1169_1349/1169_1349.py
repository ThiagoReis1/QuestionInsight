n=int(input("Quantos termos? "))
sf=0
i=0

while i<=n:
	sf+=(((-1)**i)*(i**0.5))/(9+2*i-1)
	i+=1

print(round(sf,6))