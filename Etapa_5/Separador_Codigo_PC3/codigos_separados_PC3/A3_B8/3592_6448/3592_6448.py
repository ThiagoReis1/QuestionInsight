from numpy import*
n= (eval(input("Faces tiradas no dado: ")))
t=100
i=1

while n!=[5]:
	if n==[0]:
		ponto0= t * 1 + t
	elif n==[1]:
		ponto1= t * 2 + t
	elif n == [2]:
		ponto2= (t/3) + t
		
print(round(ponto0+ponto1+ponto2),2)