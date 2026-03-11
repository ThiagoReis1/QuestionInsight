qi = int(input())
s = 0
frota = int(qi)
qc = int(input())
qd = int(input())

while(frota < 200):
	frota = frota + qc
	frota = frota - qd
	s = s+1

	
print(s)
