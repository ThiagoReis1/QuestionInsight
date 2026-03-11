from numpy import*
origem=input("Entre com a origem: ").split(',')

v=zeros(5,dtype=int)

for i in range(0, len(origem)):

	if origem[i] == "CHN":
		v[0]=v[0]+1
	if origem[i] == "JPN":
		v[1]=v[1]+1
	if origem[i] == "KOR":
		v[2]=v[2]+1
	if origem[i] == "MGL":
		v[3]=v[3]+1
	if origem[i] == "THA":
		v[4]=v[4]+1
print(max(v))
print(v)

		
		