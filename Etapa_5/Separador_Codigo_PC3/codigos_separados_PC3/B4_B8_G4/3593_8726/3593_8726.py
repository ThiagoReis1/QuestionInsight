from numpy import* 
ac = array(eval(input( "qual o ponto: ")))
i = 0 
p = 200

while i < size(ac):
	if ac[i] == 1:
		p = p / 2
	elif ac[i] == 2:
		p = p * 3
	elif ac[i] == 3 :
		p = p / 2
	elif ac[i] == 4 :
		 p = p * 3
	elif ac[i] == 5 :
		p = p / 2
	elif ac[i] == 6:
		p = p * 3 

	i+= 1 
print(round(p,2))