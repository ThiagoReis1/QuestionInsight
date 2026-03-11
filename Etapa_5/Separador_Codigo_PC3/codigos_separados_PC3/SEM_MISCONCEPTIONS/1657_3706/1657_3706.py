from numpy import*

siglas=input("").split(",")
vetor=zeros(size(siglas))
i = 0
while( i != len(siglas)):
	if(siglas[i].upper() == "AZ"):
		az= az + 1
		vetor[i]= az