import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("sample.dat")

N= data[0]

data1 =[]
data2 =[]
data3 = []
data4 =[]
x = np.linspace(0,N,N)
c =1

for i in range(0,len(data)):
    
    if(c>=N and c<=2*N):
        data2.append(data[i])
    elif(c>=2*N c<=3*N ):
        data3.append(data[i])
    elif(c>=3*N):
        data4.append(data[i])
    else:
        data.appenda(data[i])

    c = c+1

plt.scatter(x,data1)
plt.scatter(x,data2)
plt.scatter(x,data3)
plt.scatter(x,data4)
plt.show()
        
