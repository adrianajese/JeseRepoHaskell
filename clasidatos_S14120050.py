import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
import numpy as np

iris = datasets.load_iris()

especies = iris.target_names
caracteristicas = iris.data

plt.figure(1)
plt.scatter(0.1*np.random.randn(49,1),caracteristicas[0:49,2])
plt.scatter(1+0.1*np.random.randn(49,1),caracteristicas[50:99,2])
plt.scatter(2+0.1*np.random.randn(49,1),caracteristicas[100:149,2])
plt.ylabel('Longitud de Pétalo (cm)')
plt.show()

plt.figure(2)
plt.scatter(0.1*np.random.randn(49,1),caracteristicas[0:49,3])
plt.scatter(1+0.1*np.random.randn(49,1),caracteristicas[50:99,3])
plt.scatter(2+0.1*np.random.randn(49,1),caracteristicas[100:149,3])
plt.ylabel('Anchura de Pétalo (cm)')
plt.show()

plt.figure(3)
plt.scatter(0.1*np.random.randn(49,1),caracteristicas[0:49,0])
plt.scatter(1+0.1*np.random.randn(49,1),caracteristicas[50:99,0])
plt.scatter(2+0.1*np.random.randn(49,1),caracteristicas[100:149,0])
plt.ylabel('Longitud de Sépalo (cm)')
plt.show()

plt.figure(4)
plt.scatter(0.1*np.random.randn(49,1),caracteristicas[0:49,1])
plt.scatter(1+0.1*np.random.randn(49,1),caracteristicas[50:99,1])
plt.scatter(2+0.1*np.random.randn(49,1),caracteristicas[100:149,1])
plt.ylabel('Anchura de Sépalo (cm)')
plt.show()
plt.figure(5)
plt.scatter(caracteristicas[0:49,2],caracteristicas[0:49,3])
plt.scatter(caracteristicas[50:99,2],caracteristicas[50:99,3])
plt.scatter(caracteristicas[100:149,2],caracteristicas[100:149,3])
plt.xlabel('Longitud de Pétalo (cm)')
plt.ylabel('Anchura de Pétalo (cm)')
plt.show()

plt.figure(6)
plt.scatter(caracteristicas[0:49,0],caracteristicas[0:49,1])
plt.scatter(caracteristicas[50:99,0],caracteristicas[50:99,1])
plt.scatter(caracteristicas[100:149,0],caracteristicas[100:149,1])
plt.xlabel('Longitud de Sépalo (cm)')
plt.ylabel('Anchura de Sépalo (cm)')
plt.show()

plt.figure(7)
plt.scatter(caracteristicas[0:49,2],caracteristicas[0:49,0])
plt.scatter(caracteristicas[50:99,2],caracteristicas[50:99,0])
plt.scatter(caracteristicas[100:149,2],caracteristicas[100:149,0])
plt.xlabel('Longitud de Pétalo (cm)')
plt.ylabel('Longitud de Sépalo (cm)')
plt.show()

plt.figure(8)
plt.scatter(caracteristicas[0:49,3],caracteristicas[0:49,1])
plt.scatter(caracteristicas[50:99,3],caracteristicas[50:99,1])
plt.scatter(caracteristicas[100:149,3],caracteristicas[100:149,1])
plt.xlabel('Anchura de Pétalo (cm)')
plt.ylabel('Anchura de Sépalo (cm)')
plt.show()
