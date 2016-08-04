fact = [1,1]
def facts(n):
	global fact
	if (len(fact)-1)>=(n):
		return fact[n]
	else:
        	while (len(fact))!=(n+1):
            		fact.append(fact[-1]*len(fact))
        	return fact[n]

while True:
	n = input("Enter the number : ")
	print "Factorial :",facts(n)
	#print fact
	ans = raw_input("Exit(y/n):")
	if ans=="y" or ans=="Y":
        	break

"""
Output:
Enter the number : 6
Factorial : 720
Exit(y/n):n
Enter the number : 50
Factorial : 30414093201713378043612608166064768844377641568960512000000000000
Exit(y/n):y
"""
