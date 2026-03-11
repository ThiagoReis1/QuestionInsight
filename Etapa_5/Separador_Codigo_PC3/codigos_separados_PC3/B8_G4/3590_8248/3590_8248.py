from numpy import* 

k = array(eval(input("digite")))

i = 0
p = 0

while i < size(k):
	if k[i] == 1 or k[i]== 0 :
		p += 10 
	elif k[i] == 2 or k[i] == 4:
	   p+=5
	elif k[i] == 5:
		p+=20
	i+= 1 
print(p)