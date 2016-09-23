# Q1 a)

import numpy as np
import matplotlib.pyplot as plt

def phi(L):
    n = 0.0037
    a = -0.96
    L_star = 10.0**11.0
    return n*(L/L_star)**a * np.e**(-L/L_star) / L_star

x = np.linspace(10**10, 10**13, 1000000)

result = np.trapz(phi(x), x)

print result

#plt.plot(x, phi(x))
#plt.show()


# Q1 b)

def phiL(L):
    n = 0.0037
    a = -0.96
    L_star = 10.0**11.0
    return n*(L/L_star)**(a+1) * np.e**(-L/L_star)

x_0 = np.linspace(0, 10**13, 1000000)
x_10 = np.linspace(10**10, 10**13, 1000000)

result_0 = np.trapz(phiL(x_0), x_0)
plt.plot(phiL(x_10),x_10)
plt.show()
result_10 = np.trapz(phiL(x_10), x_10)
    
print result_0, result_10


