from numpy import*
v
u = zeros(size(v))
for i in range(size(v)):
	if(v[i] == "C"):
		u[1] == u[1] +1
	if(v[i] == "MC"):
		u[0] == u[0] +1
	if(v[i] == "CM"):
		u[2] == u[2] +1
	if(v[i] == "EM"):
		u[3] == u[3]+1
	if(v[i] == "E"):
		u[4] == u[4] +1
	if(v[i] == "ME"):
		u[5] == u[5]+1
print(u)
print(max(u))
	
		
	