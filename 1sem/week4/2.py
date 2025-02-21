import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(14,10))
plt.title('Номальное распределение', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
h1=np.random.normal(0,10, 50000000)
plt.hist(h1, 100, density=True, color='g',histtype='step',linewidth=2,)
h2=np.random.normal(0,10, 200000)
plt.hist(h2, 100, density=True, color='b',histtype='step',linewidth=2,)
h3=np.random.normal(0,10, 1000)
plt.hist(h3, 100, density=True, color='r',histtype='step',linewidth=2,)
plt.show()