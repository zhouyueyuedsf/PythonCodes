from scipy.misc import factorial

def Pascal(k,n):
	if k >= 0 and k <= n:
		return factorial(n) / (factorial(n-k)*factorial(k))
	else:
		return 0

for i in range(1,6):
	print('---------------------')
	for j in range(0,i+1):
		print(Pascal(j,i))