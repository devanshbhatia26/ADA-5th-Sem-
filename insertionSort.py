def insertionSort(arr):
	
	for i in range(1,len(arr)):
		temp = arr[i]
		ptr = i
		while ptr>0 and arr[ptr-1]>temp:
			arr[ptr]=arr[ptr-1]
			ptr = ptr-1
		arr[ptr]=temp
	
	return arr


arr = map(int,raw_input("Enter the space separated unsorted array : ").strip().split())
print "Sorted Array : " + " ".join(map(str,insertionSort(arr)))

# Output:
# Enter the space separated unsorted array : 5 4 3 2 1 7 8 9 
# Sorted Array : 1 2 3 4 5 7 8 9
