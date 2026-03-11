from numpy import*

string = input("string : ")
string.split(',')
string1 = ones(5,dtype=int)

i=0

while(i < size(string)):
	if(string[i] != string[i]):
		i = i + 1
	elif(string[1] == string[i]):
		string1[i] = string1[i]+1
		i = i + 1

print(max(string1))
print(string1)