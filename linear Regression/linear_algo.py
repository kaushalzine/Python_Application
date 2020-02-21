import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt



def linear():
	x=[1,2,3,4,5]
	y=[3,4,2,4,5]

	print("Independent Variable ",x)
	print("Dependent Variable   ",y)

	#y=mx+c
	#m=sum(x-x_mean)(y-y_mean)/sum(x-x_mean)
	x_mean=np.mean(x)
	y_mean=np.mean(y)

	print("x_mean ",x_mean)
	print("y_mean ",y_mean)
	N=0
	D=0
	for i in range(len(x)):
		N+=(x[i]-x_mean)*(y[i]-y_mean)
		D+=(x[i]-x_mean)**2

	m=N/D
	print("Mean   ",m)


	#c=y_mean-m*x_mean
	c=y_mean-(m*x_mean)
	print("Y intersect point(C) ",c)

	n=len(x)
	X=np.linspace(1,6,n)
	Y=c +( m * X)

	plt.plot(X,Y,color='#58b970',label="Regreation Line")
	plt.scatter(x,y,color='#ef5423',label="scatter Plot")

	plt.xlabel('X-Independant variable')
	plt.ylabel('Y-Dependant variable')

	plt.legend()
	plt.show()

	#yp=m*x+c

	#n=sum{(y-yp)**2} d=sum{(y-y_mean)**2}
	nu=0
	d=0
	for i in range(n):
		yp=(m*x[i])+c
		nu+=(y[i]-yp)**2
		d+=(y[i]-y_mean)**2
	r2=1-(nu/d)
	print("Goodness Of Fit Using R2 Method ",r2)
def main():
	print("*"*50)
	print("Linear Regreation Algo User -:")
	print("*"*50)

	linear();

if __name__=="__main__":
	main()



# output-:


# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/ML/linear Regression
# $ python linear_algo.py
# **************************************************
# Linear Regreation Algo User -:
# **************************************************
# Independent Variable  [1, 2, 3, 4, 5]
# Dependent Variable    [3, 4, 2, 4, 5]
# x_mean  3.0
# y_mean  3.6
# Mean    0.4
# Y intersect point(C)  2.4
# Goodness Of Fit Using R2 Method  0.3076923076923078

