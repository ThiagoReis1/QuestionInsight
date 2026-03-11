popP=float(input("digite a população de Pentos:"))
popB=float(input("digite a população de Bravos:"))
popPR=float(input("digite a população de Porto Real:"))
tp=float(input("digite a taxa de crescimento de Pentos:"))
tb=float(input("digite a taxa de crescimento de Bravos:"))
tpr=float(input("digite a taxa de crescimento de Porto Real:"))

t=1

povo=0

while(povo<=popPR):
	bbp=popP*tp/100
	popP=popP + bbp
	bbB=popB*tb/100
	popB=popB+bbB
	bbPR=popPR*tpr/100
	popPR=popPR+bbPR
	povo=popP+popB
	t=t+1
print(t)

