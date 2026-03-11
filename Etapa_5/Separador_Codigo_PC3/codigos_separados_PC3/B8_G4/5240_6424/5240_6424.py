c = int(input())
if 0 <= c < 100:
	t = c * 0.5 + 50
elif  100 <= c < 250:
	t = c * 0.75 + 50 
elif 250 <= c < 500:
	t = c * 1 + 50
elif 500 <= c :
	t = c * 1.25 + 50
print(round(t,2))