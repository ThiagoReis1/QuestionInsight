from numpy import*
s=input().split(",")
f=zeros(5,dtype=int)
ar=0
br=0
cl=0
co=0
uy=0
for i in range (size(s)):
	if s[i]=="ar" or s[i]=="AR":
		ar+=1
		f[0]+=1
	elif s[i]=="br" or s[i]=="BR":
		f[1]+=1
		br+=1
	elif s[i]=="cl" or s[i]=="CL":
		f[2]+=1
		cl+=1
	elif s[i]=="co" or s[i]=="CO":
		f[3]+=1
		co+=1
	elif s[i]=="uy" or s[i]=="UY":
		f[4]+=1
		uy+=1		
if ar>br and ar>cl and ar>co and ar>uy:
	print(ar)
elif  br>ar and br>cl and br>co and br>uy:
	print(br)
elif  cl>ar and cl>br and cl>co and cl>uy:
	print(cl)
elif co>ar and co>br and co>cl and co>uy:
	print(co)
else:
	print(uy)
	
print(f)
