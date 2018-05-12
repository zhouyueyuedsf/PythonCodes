import ctypes
import time

start = time.time()
ll = ctypes.cdll.LoadLibrary   
lib = ll("./libpycall.so") 
lib.dosomething(1000) 
print("**call by c++**") 
print(time.time() - start)

