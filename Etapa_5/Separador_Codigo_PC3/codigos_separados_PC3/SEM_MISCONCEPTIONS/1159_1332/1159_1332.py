tambaquis=int(input("digite o n. de tambaquis: "))
pacus=int(input("digite o n. de pacus: "))
taxa1=float(input("taxa anual de cresc de tambaquis: "))
taxa2=float(input("taxa anual de cresc de pacus: "))
nmax=int(input("n max de especies: "))

te = tambaquis + pacus
tambaquis=tambaquis*taxa1
pacus=pacus*taxa2

while(te <= 8000):
	nmax = nmax + te
print()
	
	

    
