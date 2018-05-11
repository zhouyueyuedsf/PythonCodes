import numpy as np
import matplotlib.pyplot as plt
from pylab import *
 
x = np.arange(-10.0, 10.0, 0.02)
y1 = 4*np.sin(1*x)/(1*np.pi)
y2 = 4*np.sin(3*x)/(3*np.pi)
y3 = 4*np.sin(5*x)/(5*np.pi)
y4 = 4*np.sin(7*x)/(7*np.pi)
y5 = 4*np.sin(9*x)/(9*np.pi)
y6 = 4*np.sin(11*x)/(11*np.pi)

 
plt.figure(1)
#设置x轴范围
xlim(-2.5, 2.5)
#设置y轴范围
ylim(-1, 1)

plt.subplot(211)
plt.plot(x, y1)
 
plt.subplot(211)
plt.plot(x, y2)

plt.subplot(211)
plt.plot(x, y3)

plt.subplot(211)
plt.plot(x, y4)
plt.subplot(211)
plt.plot(x, y5)
plt.subplot(211)
plt.plot(x, y6)
 
plt.subplot(212)
plt.plot(x, y1+y2+y3+y4+y5+y6)


plt.show()