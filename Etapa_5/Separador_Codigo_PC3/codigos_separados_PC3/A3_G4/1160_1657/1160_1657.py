h= input("DIgite o numero de habitantes")
v= input("Digite o numero de vampiros")
x= input("Taxa de tranformacao")
y= input("Taxa de vampiros mortos")
soma = 0
i = 0 
nv = v
nh = h
nx = x
while (nh < nv):
	ny = y *nv
	soma= soma+((nv * nh) - ny) 
	i = i + 1
print(soma)