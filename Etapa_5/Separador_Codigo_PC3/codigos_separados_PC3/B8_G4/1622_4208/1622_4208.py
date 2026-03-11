from numpy import*
et=array(eval(input("entraram:")))
s=array(eval(input("sairam:")))
num=75
i=0
tam=size(et)-1
pessoas=0
while(i<=tam and pessoas<num):

	if(i==0):
		pessoas=pessoas+et[i]
		pessoas=pessoas-s[i]
	elif(pessoas<num):
		pessoas=pessoas-s[i]
		pessoas=pessoas+et[i]
	i=i+1
	
print(pessoas)
	