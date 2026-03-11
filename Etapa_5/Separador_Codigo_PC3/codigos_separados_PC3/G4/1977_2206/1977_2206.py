s1 = input("")
s2 = input("")

if (s1 == "Investigativa") and (s2 == "Suspense"):
	print("DEXTER".upper())
elif (s1 == "Investigativa") and (s2 == "Drama"):
	print("NARCOS".upper())
elif (s1 == "Dramatica") and (s2 == "Com ficcao"):
	print("LOST".upper())
elif (s1 == "Dramatica") and (s2 == "Aventura"):
	print("SHERLOCK".upper())
else:
	print("SERIE NAO IDENTIFICADA")