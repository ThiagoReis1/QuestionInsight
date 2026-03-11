altura_joe = 1.77
taxa_joe = 0.02
at=float(input("insira altura:"))
tx= float(input("insira taxa:"))
a=0
s=0
while at<altura_joe:
	a=a+1
	altura_joe=altura_joe+taxa_joe
	at=at+tx
	s=s+1
print(s)