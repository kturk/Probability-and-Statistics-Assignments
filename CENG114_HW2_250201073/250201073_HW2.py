"""
ID = 250201073
"""
import numpy as np
from matplotlib import pyplot as plt

# Part a (Inverse Transform Method)
U = []
Xa = []
av_Xa = []
vr_Xa = []

counterA = 0
varianceSumA = 0

# Populate the given arrays.

while counterA < 50000:
    u = np.random.rand()
    U.append(u)
    
    x = u ** (1/2)
    Xa.append(x)
    
    if len(av_Xa) == 0:
        av_Xa.append(x) # If list is empty average = first number
    else:
        av_Xa.append((av_Xa[counterA-1] * len(av_Xa) + x) / (len(av_Xa) + 1) ) # Calculating new average and adding it to the list
    
    counterA = counterA + 1
    
for i in range(len(Xa)):
    varianceSumA = varianceSumA + ((Xa[i] - av_Xa[i]) ** 2)
    vr_Xa.append(varianceSumA / (i+1)) # Adding the variance to the list

# Inspect the following plots.
plt.figure()
for i in range(len(Xa)):
    plt.plot([Xa[i],U[i]],[1,1.2])

plt.figure()
hU = plt.hist(U,100,alpha=0.5,normed=True)
hXa = plt.hist(Xa,100,alpha=0.5,normed=True)
plt.figure()
plt.plot(np.cumsum(hU[0]))
plt.plot(np.cumsum(hXa[0]))

# Plot the average and variance values.

plt.figure()
plt.plot(av_Xa)
plt.title("Figure 4")
plt.figure()
plt.plot(vr_Xa)
plt.title("Figure 5")

# Part b (Rejection Method)

Xb = []
av_Xb = []
vr_Xb = []

counterB = 0
varianceSumB = 0
pdfX = 0
# Populate the given arrays.

while counterB < 50000:
    xB = np.random.rand()
    y = np.random.rand()
    pdfX = xB * 2
    
    if 2 * y <= pdfX: # Accepting the value
        Xb.append(xB)
       
        if len(av_Xb) == 0:
            av_Xb.append(xB) # If list is empty average = first number
        else:
            av_Xb.append((av_Xb[counterB-1] * len(av_Xb) + xB) / (len(av_Xb) + 1) ) # Calculating new average and adding it to the list
        
        counterB = counterB + 1

for i in range(len(Xb)):
    varianceSumB = varianceSumB + ((Xb[i] - av_Xb[i]) ** 2)
    vr_Xb.append(varianceSumB / (i+1)) # Adding the variance to the list
        
# Inspect the following plots.

plt.figure()
hXb = plt.hist(Xb,100,normed=True)
plt.figure()
plt.plot(np.cumsum(hXb[0]))

# Plot the average and variance values.

plt.figure()
plt.plot(av_Xb)
plt.title("Figure 8")
plt.figure()
plt.plot(vr_Xb)
plt.title("Figure 9")
