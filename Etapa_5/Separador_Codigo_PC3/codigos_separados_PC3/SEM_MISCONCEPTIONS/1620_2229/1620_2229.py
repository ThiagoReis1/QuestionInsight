from numpy import*

tban=array(eval(input("tempo no banho: ")))
ptorn=array(eval(input("tempo aberto: ")))
w=0
gasto=0
while(w<size(tban)):
	gasto=gasto+5*tban[w]*ptorn[w]/100
	w=w+1
	
print(round(gasto,2))
