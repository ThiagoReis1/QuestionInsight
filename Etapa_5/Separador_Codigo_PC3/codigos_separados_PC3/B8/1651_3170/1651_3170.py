from numpy import*
origem= input("").split(',')
res=zeros(6, dtype=int)

for i in range(size(origem)):
	if(origem[i]=='MC'):
		res[0]+=1
	elif(origem[i]=='C'):
		res[1]+=1
	elif(origem[i]=='CM'):
		res[2]+=1
	elif(origem[i]=='EM'):
		res[3]+=1
	elif(origem[i]=='E'):
		res[4]+=1
	elif(origem[i]=='ME'):
		res[5]+=1
num_max=max(res)
print(num_max)
print(res)