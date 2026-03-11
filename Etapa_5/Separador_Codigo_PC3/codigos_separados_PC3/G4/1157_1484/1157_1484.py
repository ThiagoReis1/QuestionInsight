tamb = int(input("n° de peixes no tanque: "))
taxa = int(input("taxa de crescimento:"))
ret = int(input("n° retirada de peixes"))
an = 0

while(tamb > 0 ):
	tamb = (taxa*tamb)/100 + tamb
	an = an + 1
	tamb = tamb - ret
print(an)