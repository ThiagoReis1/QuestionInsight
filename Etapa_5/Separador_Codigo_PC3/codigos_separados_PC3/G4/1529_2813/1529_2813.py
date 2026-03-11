qi = int(input("quantidade inicial de guerreirosÇ  "))
qc = int(input("cavalaria"))
pi = int(input("percentual infantaria"))
pc = int(input("percentual cavalaria"))

i = 1

aqi= qi
aqc = qc
somat = 0
soma1 = 1
soma2 = 1
while(somat <= 50000):
	soma1 = soma1 + aqi + (aqi*(pi/100)) 
	soma2 = soma2 + aqc + (aqc*(pc/100))
	somat = soma1+soma2
	i = i + 1
	
print(i)