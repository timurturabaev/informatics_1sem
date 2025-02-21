import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
df = pd.read_csv('iris_data.csv')
x1=list(df['Species'])
x11=list(df['Species'])
k=len(x1)
for i in range(1,k):
    if x1[i-1]==x1[i]:
        x1[i-1]=0
for i in range(x1.count(0)):
    x1.remove(0)
y1=[0]*len(x1)
for i in range(len(x1)):
    y1[i]=x11.count(x1[i])
ax1.pie(y1,labels=x1)
x2=list(df['PetalLengthCm'])
for i in range(len(x2)):
    if x2[i]<1.2:
        x2[i]=1
    elif x2[i]>=1.5:
        x2[i]=3
    else:
        x2[i]=2
y2=[x2.count(1),x2.count(2),x2.count(3)]
ax2.pie(y2,labels=['Длина лепестка меньше 1,2 см','Длина лепестка больше или равна 1,2 см и меньше 1,5см','Длина лепестка больше или равна 1,5 см'])
#plt.savefig('krug.png', dpi=300)
plt.show()