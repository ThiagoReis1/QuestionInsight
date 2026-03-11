l = str(input("digite o nucleotideo:")) .upper()
S = 0
A = 0
G = 0
C = 0
qnA = 0

while(l != S):
	if((l == A) or (l == G) or (l == C) or (l == S)):
		qnA = qnA + 1
		l = str(input("digite o nucleotideo:")) .upper()
	else:
		qnA = qnA + 1
		print(qnA)
	
	
	
	