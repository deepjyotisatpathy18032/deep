#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np
X= [245.31,210.41,163.96, 202.72, 160.34, 251.70, 330.72, 344.09, 352.63, 41.05, 5.67, 28.75, 3.13, 27.12, 42.29, 359.73, 57.50, 10.92, 47.77, 103.39, 91.36]
Y= [-42.09, -9.30, 20.25, 21.35, 50.43, 40.34, 22.12, 16.67, 20.19, 38.27, 21.21, 25.22, 6.02, 17.74, 3.06, -19.59, -0.28, -45.43, -42.08, -14.00, -42.36]
Z = [2.64, 38.77, 18.24, 30.24, 9.02, 6.39, 13.56, 52.31, 34.49, 18.41, 62.41, 15.99, 9.61, 33.79, 13.29, 10.39, 71.01, 4.58, 8.99, 13.72, 21.89]


y,x = np.meshgrid(np.linspace(-100,100,201), np.linspace(0,1000,1001))
z = [[0 for col in range(200)] for row in range(1000)]


for i in range(len(Z)):
    a = int(X[i])
    b = int(Y[i])
    z[int(x[a][1])][int(y[1][b])] = Z[i]
   



z_max= np.abs(z).max()
fig, ax = plt.subplots()
c = ax.pcolormesh(x,y,z, cmap = 'gist_rainbow', vmin=0, vmax=z_max)
ax.axis([x.min(),x.max(),y.min(),y.max()])                         
fig.colorbar(c, ax=ax)
plt.show()




# # Code with little enlarged points

# In[2]:


import matplotlib.pyplot as plt
import numpy as np
X= [245.31,210.41,163.96, 202.72, 160.34, 251.70, 330.72, 344.09, 352.63, 41.05, 5.67, 28.75, 3.13, 27.12, 42.29, 359.73, 57.50, 10.92, 47.77, 103.39, 91.36]
Y= [-42.09, -9.30, 20.25, 21.35, 50.43, 40.34, 22.12, 16.67, 20.19, 38.27, 21.21, 25.22, 6.02, 17.74, 3.06, -19.59, -0.28, -45.43, -42.08, -14.00, -42.36]
Z = [2.64, 38.77, 18.24, 30.24, 9.02, 6.39, 13.56, 52.31, 34.49, 18.41, 62.41, 15.99, 9.61, 33.79, 13.29, 10.39, 71.01, 4.58, 8.99, 13.72, 21.89]


y,x = np.meshgrid(np.linspace(-100,100,201), np.linspace(0,1000,1001))
z = [[0 for col in range(200)] for row in range(1000)]


for i in range(len(Z)):
    a = int(X[i])
    b = int(Y[i])
    for j in range (20):
        for k in range (4):
            z[int(x[a+j][1])][int(y[1][b+k])] = Z[i]
   



z_max= np.abs(z).max()
fig, ax = plt.subplots()
c = ax.pcolormesh(x,y,z, cmap = 'gist_rainbow', vmin=0, vmax=z_max)
ax.axis([x.min(),x.max(),y.min(),y.max()])                         
fig.colorbar(c, ax=ax)
plt.show()



# In[ ]:




