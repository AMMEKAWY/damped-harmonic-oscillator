#--------damped oscillator---------------


#---------importing modules-------------
import numpy as np
import matplotlib.pyplot as plt

#-------------------------------------------
#---------defining quantities---------------
#------------------------------------------

b=0.1
m=5 #kg
l=0.2 #m
gamma= 3*b/(m*(l**2))
g=9.8 #m/s**2
w= np.sqrt((3*g)/(2*l))


theta=[np.pi/4]  #angle list
u=[0]            #velocity list

i=0
ti=0    #initial time
tf=10   #final time
h=(tf-ti)/100000  #s  time step
t=[ti]          #time list

#------------------------------------------------
#----------Euler's method for solving ODE's------
#------------------------------------------------


while round(ti,1) != tf:
    theta.append(u[i]*h+theta[i])
    u.append(-h*(gamma*u[i]+(w**2)*theta[i])+u[i])
    t.append(ti+h)
    ti=ti+h
    i+=1

#-------------------------------------------------
#---------plotting the results--------------------
#-------------------------------------------------

plt.plot(t,theta)
plt.show()



