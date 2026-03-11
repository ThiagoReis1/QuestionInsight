qi = int(input("quantidade inicial de baloes"))
qc = int(input("novos baloes"))
qd = int(input("baloes destruidos"))

total = qi
s = 0
while( total < 200 ):
	total = qi - qd + qc
	s = s + 1
	if ( total < 200):
		total = total - qd + qc
		s= s + 1
	else:
		print(s)