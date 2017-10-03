
def merge(arr, low, mid, high):
	n1 = mid - low + 1
	n2 = high - mid

	L = [0] * (n1)
	R = [0] * (n2)

	for i in range(0 , n1):
		L[i] = arr[low + i]

	for j in range(0 , n2):
		R[j] = arr[mid + 1 + j]

	i = 0
	j = 0
	k = low

	while i < n1 and j < n2 :
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1


	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1


def mergeSort(arr,low,high):
	if low < high:
		mid = (low+(high-1))/2

		mergeSort(arr, low, mid)
		mergeSort(arr, mid+1, high)
		merge(arr, low, mid, high)

n=int(raw_input())
line =  raw_input().split()
arr = [int(i) for i in line]
arr.reverse()
mergeSort(arr,0,n-1)
for i in range(n):
	print ("%d" %arr[i]),

