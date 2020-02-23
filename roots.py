# -*- coding: utf-8 -*-
from bisection import *
import numpy


import matplotlib.pyplot as plt


def f(x):
	return x**3 - 3.23*x**2- 7.73*x + 9.84

x = bisection(f,0.0,1.005,tol = 1.0e-9)
print('x=','{:6.4f}'.format(x))
def plot():
    X = numpy.linspace(0.9,1,num=100)
    fx = []
    for i in numpy.arange(len(X)):
         fx.append(X[i]**3 - 3.23*X[i]**2 - 7.73*X[i] + 9.84)
    dotx=numpy.array([x])
    doty=numpy.array([0])
    plt.plot(X,fx)
    plt.scatter(dotx,doty)
    plt.grid()
    plt.axvline()
    plt.axhline()
    plt.show()
plot()