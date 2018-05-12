import time

def dosomething(n):
	for i in range(n):
		i *= 2

start = time.time()
dosomething(1000)
print("**call by python**")
print(time.time() - start)