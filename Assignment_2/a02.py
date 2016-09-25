import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


## Q1 a)

def phi(L):
    n = 0.0037
    a = -0.96
    L_star = 10.0**11.0
    return n*(L/L_star)**a * np.e**(-L/L_star) / L_star

x = np.linspace(10**10, 10**13, 1000000)

result = np.trapz(phi(x), x)

print "space density:", result


## Q1 b)

def phiL(L):
    n = 0.0037
    a = -0.96
    L_star = 10.0**11.0
    return n*(L/L_star)**(a+1) * np.e**(-L/L_star)

x_0 = np.linspace(0, 10**13, 1000000)
x_10 = np.linspace(10**10, 10**13, 1000000)

result_0 = np.trapz(phiL(x_0), x_0)
result_10 = np.trapz(phiL(x_10), x_10)
    
print "L > 0 luminosity density:", result_0
print "L > L_star luminosity density:", result_10


## Q2

log_cz = np.array([3.958, 4.066, 4.223, 3.992, 4.137, 3.897, 3.891, 4.481, 3.774, 4.240, 3.736, 4.326])
m = np.array([16.4090, 17.3488, 17.8124, 16.3683, 17.2548, 16.2426, 16.2164, 19.0955, 15.4026, 17.7777, 15.4329, 18.4524])

# Linear regression to find best fit line:
slope, intercept, r_value, p_value, std_err = stats.linregress(log_cz, m)

std_dev = np.std(m)

print "r_squared with fitted slope:", r_value**2
print "fitted slope:", slope
print "intercept with fitted slope:", intercept

# Do it for fixed slope of 5.0:
slope_fixed = 5.0
intercepts_fixed = m - slope_fixed*log_cz
intercept_fixed = np.mean(intercepts_fixed)

std_intercepts = np.std(intercepts_fixed)

print "intercept with fixed slope:", intercept_fixed

print "standard deviation of magnitudes:", std_dev
print "standard deviation of intercepts:", std_intercepts

lobf_fit = slope*log_cz + intercept
lobf_fixed = slope_fixed*log_cz + intercept_fixed

points = plt.scatter(log_cz, m, s = 2, color='b')
line1 = plt.plot(log_cz, lobf_fit)
line2 = plt.plot(log_cz, lobf_fixed)
plt.setp(line1, color='r', linewidth=0.3)
plt.setp(line2, color='g', linewidth=0.3)
plt.title('$m_{max}$ vs log$_{10}$($\\frac{cz}{[km/s]}$)')
plt.ylabel('$m_{max}$')
plt.xlabel('log$_{10}$($\\frac{cz}{[km/s]}$)')
plt.savefig('a02q2ae.png')
