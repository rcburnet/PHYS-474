import numpy as np
import scipy.constants as con
import sys

# Q3

def f(x):
    return -(x+1)**2.0*np.log(x+1)+2*x*(x+1)-x

def bisection(start,stop,tolerance):
    mid = (start+stop)/2.0
    while (stop-start)/2.0 > tolerance:
        if f(mid) == 0:
            return mid
        elif f(start)*f(mid) < 0:
            stop = mid
        else :
            start = mid
        mid = (start+stop)/2.0	
    return mid

print "Root of q3 is: ", bisection(1,3,0.000001)


# Q6

r_v = np.array([96.0,206.0,2060.0])
c = np.array([9.0,7.14,3.55])
delta_c = np.array([34600.0,20000.0,4050.0])

def M_rv(r_v,c,delta_c):
    return 4*np.pi*(r_v/c)**3.0*delta_c*136*(np.log(c+1)+1/(c+1)-1)

def rho(delta_c,c):
    return 3*delta_c*136*(np.log(c+1)+1/(c+1)-1)/c**3.0

def V_max(r_v,c,delta_c):
    return 0.465*(r_v/c)*np.sqrt(4*np.pi*con.G*delta_c*136*1.989e30/(3.086e19**3.0))*3.086e16

def r(r_v,c):
    return 2.16258*r_v/c

def sigma_r(r_v,c,delta_c):
    return (r_v/c)*np.sqrt(4*np.pi*con.G*delta_c*136*1.989e30/(3.086e19**3.0))*np.sqrt((1/2.0-np.log(c+1)/(c+1)-1/(2*(c+1)**2.0))/((np.log(c+1)+1/(c+1)-1)))*3.086e16

print "Enclosed mass within viral radius: ", M_rv(r_v,c,delta_c)
print "Mean density within viral radius: ", rho(delta_c,c)
print "Maximum circular velocity: ",V_max(r_v,c,delta_c)
print "Radius at maximum circular velocity: ", r(r_v,c)
print "line of sight velocity dispersion: ", sigma_r(r_v,c,delta_c)
