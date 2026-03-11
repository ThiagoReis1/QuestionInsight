from numpy import*
n = array(eval(input("Quais as notas a serem verificadas? ")))
i=0
while i<size(n):
	#if n[i] == 4.0 and n[i] == 4.1 and n[i]== 4.2 and n[i]==4.3 and v[i]==4.4 and n[i]==4.5 and n[i]== 4.6 and n[i]==4.7 and n[i]==4.8 and n[i]==4.9 and n[i]==5.0:
		#n[i]==4.0
	#if n[i]==9.0 and n[i]== 9.1 and n[i]==9.2 and n[i]==9.3 and n[i]==9.4 and n[i]==9.5 and n[i]==9.6 and n[i]==9.7 and n[i]==9.8 and n[i]==9.9 and n[i]==10.0:
		#n[i]==10.0
	if n[i]>=4.0 and n[i]<5.0:
		n[i]=4.
	if n[i]>=9.0 and n[i]<10.0:
		n[i]=10.
	i=i+1
print(n)