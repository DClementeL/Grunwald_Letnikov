import numpy as np
import matplotlib.pyplot as plt

# Test version, Daniel Clemente Lopez

q = 0.99; h = 0.005; hq = pow(h,q)
	
tf = 30; n = int(tf/h) +1

x = np.zeros(n); y = np.zeros(n); z = np.zeros(n)
x[0], y[0], z[0] = 1 , 0 , 1
	
a ,b ,c = 10, 28, 8/3

Cq = np.zeros(n)
Cq[0] = 1

for j in range (1,n):
	Cq[j] = (1 -(1+q)/j)*Cq[j-1]

for k in range(1,n):
	sum1, sum2, sum3 = 0 , 0 ,0

	for j in range (1,k+1):
		sum1 = sum1 + Cq[j]*x[k-j]
		sum2 = sum2 + Cq[j]*y[k-j]
		sum3 = sum3 + Cq[j]*z[k-j]

	x[k] = hq*( a*(y[k-1]-x[k-1]) ) 		 	- sum1 
	y[k] = hq*( x[k-1]*(b-z[k-1]) - y[k-1]  )   - sum2
	z[k] = hq*(x[k-1]*y[k-1]-c*z[k-1])		 	- sum3

	

	
plt.plot(x,z)
plt.show(block=False)
input('Press Enter to quit')
plt.close()
