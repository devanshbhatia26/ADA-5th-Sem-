def merge(a,b):
	
	ptra = 0
	ptrb = 0

	arr = []
	while ptra<len(a) and ptrb<len(b):
		if a[ptra]<b[ptrb]:
			arr.append(a[ptra])
			ptra+=1
		else:
			arr.append(b[ptrb])
			ptrb+=1
	while ptra<len(a):
		arr.append(a[ptra])
		ptra+=1
	while ptrb<len(b):
		arr.append(b[ptrb])
		ptrb+=1

	return arr

def mSort(arr):
	if len(arr)==1:
		return arr
	else:
		l = len(arr)
		a = mSort(arr[:(l/2)])
		b = mSort(arr[(l/2):])
		return merge(a,b)

arr = map(int,raw_input("Enter the space separated unsorted array : ").strip().split())
print "Sorted Array : " + " ".join(map(str,mSort(arr)))

# Output:
# Enter the space separated unsorted array :  4 5 6 1 2 4 5 9 8 7
# Sorted Array : 1 2 4 4 5 5 6 7 8 9
