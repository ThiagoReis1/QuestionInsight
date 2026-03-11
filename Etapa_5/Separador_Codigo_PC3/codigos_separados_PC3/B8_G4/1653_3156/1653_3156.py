from numpy import*
o=input("").split(',')
i=0
res=zeros(5, dtype=int)
for i in range(size(o)):
	if(o[i]=='AR'):
		res[0]+=1
	elif(o[i]=='BR'):
		res[1]+=1
	elif(o[i]=='CL'):
		res[2]+=1
	elif(o[i]=='CO'):
		res[3]+=1
	elif(o[i]=='UY'):
		res[4]+=1
nm=max(res)
print(nm)
print(res)