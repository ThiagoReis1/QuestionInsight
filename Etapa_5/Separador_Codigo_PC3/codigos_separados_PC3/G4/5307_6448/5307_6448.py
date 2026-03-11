     #(1*i+1) (-1)**i
x= float(input("numero real x: "))
k = int(input("numero inteiro k: ")) # quantidade de termos

#k / x
s=0
i = 0
while (k!=i):
	#termo1= 1*i+1
	#i=i+1
	s= s + (1*i+1/x)
	i= i+1
print(round(s,10))

