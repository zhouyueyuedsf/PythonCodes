import math
def mergeSort(A, p, r):
	if p < r:
		q = math.floor((p+r)/2)
		mergeSort(A, p, q)
		mergeSort(A, q+1, r)
		merge(A, p, q, r)

def merge(A, p, q, r):
	a = []
	b = []
	for i in range(p, q):
		a.append(A[i])
	a.append(9999)
	for j in range(q, r+1):
		b.append(A[j])
	b.append(9999)
	m = 0
	n = 0
	count = 0
	while(1):
		if count == len(A):
			break
		if a[m] <= b[n]:
			A[count] = a[m]
			m = m + 1
		else:
			A[count] = b[n]
			n = n + 1
		count += 1

				

a = [1,3,4,9,2,6,7,8]
mergeSort(a, 0, 7)
print(a)