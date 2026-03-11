rs= input ('').upper()

num = 0 
q = 0 

while rs != 'S' :
	if rs == 'PRETA':
		q += 1 
	num += 1 
	
	rs = input('').upper()	

print(q)