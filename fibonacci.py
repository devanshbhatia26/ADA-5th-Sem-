fib = [0,1]
#Assuming that 1st fibonacci number is 1
def fibs(n):
	global fib
	if (len(fib)-1)>=(n):
		return fib[n]
	else:
        	while (len(fib))!=(n+1):
            		fib.append(fib[-1]+fib[-2])
        	return fib[n]

while True:
	n = input("Enter the number : ")
	print fibs(n)
	ans = raw_input("Exit(y/n):")
	if ans=="y" or ans=="Y":
        	break

""" 
Output : 
Enter the number : 5
5
Exit(y/n):n
Enter the number : 10
55
Exit(y/n):n
Enter the number : 60
1548008755920
Exit(y/n):y
"""
