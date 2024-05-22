import numpy as np
import flet as ft
from flet import Page, TextField, Dropdown, ElevatedButton, Row, Text

def Gausito(page: Page):
    
    page.bgcolor = "#46FBA9"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    click = ElevatedButton(text='Conversiones', scale=2, on_click=btn_click)
    fila_boton_click = Row([click])
    fila_boton_click.alignment = 'center'
    
    def btn_click():
        n = minipana.value
        ElpanitaGauss(n)

    page.add(fila_boton_click, Row(alignment=ft.MainAxisAlignment.CENTER, width=70, height=80) , fila_boton_click2)
    
class ElpanitaGauss:
    def __init__(self, n):
        self.n = n
        self.matriz = np.zeros((n, n+1))
        self.solucion = np.zeros(n)

    def ingresar_coeficientes(self):
        matriz_datos = []
        for control in contenedores_matriz:
            if isinstance(control, ft.Row):
                fila = []
                for txt in control.controls:
                    if isinstance(txt, ft.TextField):
                        fila.append(float(txt.value))
                matriz_datos.append(fila)
        return matriz_datos

    def gauss_jordan(self):
        for i in range(self.n):
            if self.matriz[i][i] == 0.0:
                print("Error, no tiene solución")
                return

            for j in range(self.n):
                if i != j:
                    ratio = self.matriz[j][i] / self.matriz[i][i]

                    for k in range(self.n+1):
                        self.matriz[j][k] = self.matriz[j][k] - ratio * self.matriz[i][k]

        for i in range(self.n):
            self.solucion[i] = self.matriz[i][self.n] / self.matriz[i][i]

    def getSolucion(self):
        return self.solucion

# Crear una instancia del sistema de ecuaciones
n = int(input('Ingrese la cantidad de datos: '))
sistema = SistemaEcuaciones(n)

# Ingresar coeficientes
sistema.ingresar_coeficientes()

# Resolver el sistema
sistema.gauss_jordan()

# Imprimir la solución
sistema.imprimir_solucion()
