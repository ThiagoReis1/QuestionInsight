x=float(input("x: "))
k=int(input("k: "))
sen=x
i=1
l=3
while(i<k):
	sen=sen+((x**l)/(l))*(-1)**i
	i=i+1
	l=l+2
print(round(sen,6))