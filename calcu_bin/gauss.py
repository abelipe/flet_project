import numpy as np
import flet as ft
from flet import Page, TextField, Dropdown, ElevatedButton, Row, Text

def Gausito(page: Page):
    
    page.bgcolor = "#009999"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    
    rand = ElevatedButton(text='Random', scale=2)
    rand_boton_click = Row([rand])
    rand_boton_click.alignment = 'center'
    
    calcular = ElevatedButton(text='Calcular', scale=2)
    boton_click = Row([rand, calcular])
    boton_click.alignment = 'center'
    boton_click.spacing = 200
    
    tamano = TextField(label='Ingrese un numero')
    textf = Row([tamano])
    textf.alignment = 'center'
    matriz = TextField(label='AB matriz chamin:', disabled=True, multiline=True,min_lines=2, max_lines=100, color='#000000')
    solucion = TextField(label='Solución de X:', disabled=True, multiline=True,min_lines=2, max_lines=10, color='#000000')
    
    def btn_clickrandom(event):
        try:
            n = int(tamano.value)
            if n>10:
                solucion.value = 'La matriz queda muy grande y puede lagear todo mira linea 30 de gauss.py'
                page.update()
                return
            A = np.random.randint(1, 10, size=(n, n))
            B = np.random.uniform(1, 99, size=(n, 1)).round(2)
            gauss = ElpanitaGauss(A, B)
            matriz.value = str(gauss.getAB0())
            solucion.value = str(gauss.getSolucion())
            page.update()
        except:
            solucion.value ='Porfavor colocar un valor correcto'
            
    def btn_clickcalcular(event):
        n = int(tamano.value)
        
        
    rand.on_click = btn_clickrandom
    calcular.on_click = btn_clickcalcular
    page.add(textf, Row(alignment=ft.MainAxisAlignment.CENTER, width=70, height=80) , boton_click, Row(alignment=ft.MainAxisAlignment.CENTER, width=70, height=80), matriz, solucion)
    
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