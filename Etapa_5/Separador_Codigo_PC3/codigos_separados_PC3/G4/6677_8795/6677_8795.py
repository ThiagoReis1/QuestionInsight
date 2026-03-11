from numpy import*
lst=[]
for _ in range(10):
	lst=lst+[int(input())]
soma = int(input())
lst1=[k for k in lst if k>=soma]
print(len(lst1))
print(array(lst1, dtype=float))