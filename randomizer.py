#Random number generator base of a pi and cpu time

#9.550561797752808%  Chances for 0
#11.025280898876405% Chances for 1
#10.182584269662922% Chances for 2
#10.042134831460674% Chances for 3
#9.410112359550562%  Chances for 4
#10.042134831460674% Chances for 5
#9.480337078651685%  Chances for 6
#9.620786516853933%  Chances for 7
#9.97191011235955%   Chances for 8
#10.674157303370785% Chances for 9
#0.000000000000002%  missing due to rounding by the computer

import time as t

#--------
#Implemetation of the Bailey–Borwein–Plouffe (BBP) algorithm to calculate digits of py
#Credit: Fermat's Library on Twitter
from decimal import Decimal
from decimal import getcontext

def pi(precision):
    getcontext().prec=precision
    return sum(1/Decimal(16)**k * 
        (Decimal(4)/(8*k+1) - 
         Decimal(2)/(8*k+4) - 
         Decimal(1)/(8*k+5) -
         Decimal(1)/(8*k+6)) for k in range (precision))
#--------

def rand():
    #Turns all the 1424 after the comma in py into a list of integers
    pilist = [int(i) for i in [*str(pi(1424))[2:]]]
    #gets CPU time after the comma since last Epoch and multiplies it by 1500 and rounts it with int() to get a number inbetween 0 and 1423 that changes every millisecond
    time = int(((t.time())-int((t.time())))*1423)
    return pilist[time]

print(rand())
