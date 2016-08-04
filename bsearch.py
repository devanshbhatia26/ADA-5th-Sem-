arr = map(int,raw_input("Enter the space separated array : ").strip().split())
def bsearch(arr, num):
	f = 0
	l = len(arr)-1
	flag = False
	while f<=l and not flag:
		mid = (f + l)/2
	        if arr[mid] == num:
	        	flag = True
			break
	        else:
	        	if num < arr[mid]:
	        		l = mid-1
	        	else:
	        		f = mid+1
	if arr[mid]==num:
		print "Found at index : ",mid
	else:
		print "Not Found"	

while True:
	num = input("Enter the number to be found : ")
	bsearch(arr,num)
	ans = raw_input("Search another number(y/n): ")
	if ans=="n" or ans=="N":
		break

"""
Output:
Enter the space separated array : 5 10 15 20 25
Enter the number to be found : 5
Found at index :  0
Search another number(y/n): y
Enter the number to be found : 15
Found at index :  2
Search another number(y/n): y
Enter the number to be found : 25
Found at index :  4
Search another number(y/n): n
"""
