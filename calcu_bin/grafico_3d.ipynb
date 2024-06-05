import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
class ElpanitaGauss:
    def __init__(self, A, B):
        # evitar error en operaciones
        self.A = np.array(A, dtype=float)

        # matriz aumentada
        self.AB = np.concatenate((self.A, B), axis=1)
        self.AB0 = np.copy(self.AB)

        # eliminacion hacia adelante
        self.AB = self.eliminacion_hacia_adelante(self.AB)

        # eimina hacia atras
        self.AB = self.eliminacion_hacia_atras(self.AB)

        # solución de X
        self.X = self.solucion(self.AB)



    def pivoteo_parcial_por_filas(self, AB):
        tamaño = np.shape(self.AB)
        n = tamaño[0]
        m = tamaño[1]

        # para cada fila en AB
        for i in range(0, n-1):  # columna desde diagonal i en adelante
            columna = abs(self.AB[i:, i])
            dondemax = np.argmax(columna)

        return AB


    def eliminacion_hacia_adelante(self, AB):
        tamaño = np.shape(self.AB)
        n = tamaño[0]
        m = tamaño[1]

        for i in range(0, n-1):
            pivote = self.AB[i, i]
            
            if self.AB[i][i] == 0.0: #chequear que si tenga solucion la eliminacion
                return
            
            adelante = i + 1
            for k in range(adelante, n, 1):
                factor = self.AB[k, i]/pivote
                self.AB[k, :] = self.AB[k, :] - self.AB[i, :]*factor

        return AB


    def eliminacion_hacia_atras(self, AB):
        tamaño = np.shape(self.AB)
        n = tamaño[0]
        m = tamaño[1]

        ultfila = n-1
        ultcolumna = m-1
        for i in range(ultfila, 0-1, -1):
            pivote = self.AB[i, i]
            atras = i-1
            for k in range(atras, 0-1, -1):
                factor = self.AB[k, i]/pivote
                self.AB[k, :] = AB[k, :] - AB[i, :]*factor

        # diagonal a unos
        for i in range(n):
            self.AB[i, :] = self.AB[i, :]/AB[i, i]

        return self.AB


    def solucion(self, AB):
        tamaño = np.shape(self.AB)
        n = tamaño[0]
        m = tamaño[1]

        self.X = np.copy(self.AB[:, m-1])
        self.X = np.transpose([self.X])
        return self.X
    
    def getSolucion(self):
        return self.X
    
    def getAB(self):
        return self.AB
    def getAB0(self):
        return self.AB0
n = int(input("Colocar el tamaño de la matriz: "))

A = np.random.randint(1, 10, size=(n, n))
B = np.random.uniform(1, 99, size=(n, 1)).round(2)
gauss = ElpanitaGauss(A, B)
print("Solucion de gauss")
v = gauss.getSolucion()
solucioncita = np.transpose(v)
s = np.linalg.norm(solucioncita)
print(solucioncita)



x = np.arange(n)
y = np.arange(n)
x , y = np.meshgrid(x, y)
z = solucioncita

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.plot_surface(x, y, z, cmap = "hot")
plt.show()
