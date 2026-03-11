from numpy import*
v1 = array(eval(input("danos: ")))
v2 = arange(len(v1))
v3 = zeros(len(v1))
i = 0


while (i < len(v1)):
	v3[i] = (v2[i] + 1) * v1[i]
	i = i + 1
print(int(sum(v3)))