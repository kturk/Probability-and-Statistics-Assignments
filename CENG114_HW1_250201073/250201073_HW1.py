"""
ID = 250201073
"""

from matplotlib import pyplot as plt
import numpy as np

listFor6 = []
listFor4 = []
listForToss = []
listForX = []
listFor6Mean = []
listFor4Mean = []
listForTossMean = []
listForXMean = []
listForVarianceX = []

counter = 0
totalX = 0
meanX = 0
varianceSum = 0
A = 0
B = 0
C = 0 
ExpecA = 0
ExpecB = 0
ExpecC = 0

while counter < 100000:
    randomFor6 = np.random.rand()
    randomFor4 = np.random.rand()
    randomForToss = np.random.rand()

    if (0 <= randomFor6 < 1/6):
        A = 1
    elif (1/6 <= randomFor6 < 2/6):
        A = 2
    elif (2/6 <= randomFor6 < 1/2):
        A = 3
    elif (1/2 <= randomFor6 < 4/6):
        A = 4
    elif (4/6 <= randomFor6 < 5/6):
        A = 5
    elif (5/6 <= randomFor6 < 1):
        A = 6
    
    ExpecA = 1*1/6 + 2*1/6 + 3*1/6 + 4*1/6 + 5*1/6 + 6*1/6
    listFor6.append(A)
    
    if len(listFor6Mean) == 0:
        listFor6Mean.append(A) # If the list empty just append the A as a first entry
    else:
        listFor6Mean.append(((listFor6Mean[counter-1]*len(listFor6Mean)) + A) / (len(listFor6Mean) + 1)) # Calculating new mean with new A and adding it to list
    
    if (0 <= randomFor4 < 1/4):
        B = 1      
    elif (1/4 <= randomFor4 < 1/2):
        B = 2        
    elif (1/2 <= randomFor4 < 3/4):
        B = 3 
    elif (3/4 <= randomFor4 < 1):
        B = 4
    
    ExpecB = 1*1/4 + 2*1/4 + 3*1/4 + 4*1/4
    listFor4.append(B)
    
    if len(listFor4Mean) == 0:
        listFor4Mean.append(B) # If the list empty just append the B as a first entry
    else:
        listFor4Mean.append(((listFor4Mean[counter-1]*len(listFor4Mean)) + B) / (len(listFor4Mean) + 1)) # Calculating new mean with new B and adding it to list
    
    if (0 <= randomForToss < 1/2):
        C = 1
    elif (1/2 <= randomForToss < 1):
        C = -1
    
    ExpecC = 1*1/2 + (-1)*1/2
    listForToss.append(C)
    
    if len(listForTossMean) == 0:
        listForTossMean.append(A) # If the list empty just append the C as a first entry
    else:
        listForTossMean.append(((listForTossMean[counter-1]*len(listForTossMean)) + C) / (len(listForTossMean) + 1)) # Calculating new mean with new C and adding it to list

    X = A + B * C
    
    listForX.append(X)
    
    if len(listForXMean) == 0:
        listForXMean.append(X)
    else:
        listForXMean.append(((listForXMean[counter-1]*len(listForXMean)) + X) / (len(listForXMean) + 1)) # Calculating new mean with new X and adding it to list

    
    counter = counter + 1
    

i = 0
for j in range(len(listForX)):
    varianceSum = varianceSum + (listForX[j] - listForXMean[i]) ** 2
    if j == i:
        varianceX = varianceSum / (j+1) # Calculating the variance
        listForVarianceX.append(varianceX) # Adding the variance to the list
        i = i + 1
        continue


plt.title("Graph of A")
plt.hist(listFor6,100)
plt.show()
plt.title("Graph of B")
plt.hist(listFor4,100)
plt.show()
plt.title("Graph of C")
plt.hist(listForToss,100)
plt.show()
plt.title("Graph of X")
plt.hist(listForX,100)
plt.show()

plt.title("Graph of A's mean")
plt.plot(listFor6Mean)
plt.show()
plt.title("Graph of B's mean")
plt.plot(listFor4Mean)
plt.show()
plt.title("Graph of C's mean")
plt.plot(listForTossMean)
plt.show()
plt.title("Graph of X's mean")
plt.plot(listForXMean)
plt.show()

plt.title("Graph of Variance")
plt.plot(listForVarianceX)
plt.show()