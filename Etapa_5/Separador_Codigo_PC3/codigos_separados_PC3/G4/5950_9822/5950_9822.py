tp = input()
qttp = int(input())
qtcap = int(input())

T = 6
P = 5
C = 4.5

if tp == "T":
	total = ( qttp * T ) + ( qtcap * C )
else:
	total = ( qttp *  P ) + ( qtcap * C )
	
print(round(total,1))