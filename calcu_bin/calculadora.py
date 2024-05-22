import numpy as np
import flet as ft
from flet import Page, TextField, Dropdown, ElevatedButton, Row, Text
import random

def traductor(page: Page):
    page.title = 'Transformador DL'
    
    numero = TextField(label='Ingrese un numero')
    resultado = TextField(label='Resultado', value = 0)
    down_1 = Dropdown(width=135, options=[ft.dropdown.Option('Binario'), ft.dropdown.Option(
        'Ternario'), ft.dropdown.Option('Cuartenario'), ft.dropdown.Option('Octal'), ft.dropdown.Option('Decimal'), ft.dropdown.Option('Hexadecimal')],)
    down_2 = Dropdown(width=135, options=[ft.dropdown.Option('Binario'), ft.dropdown.Option(
        'Ternario'), ft.dropdown.Option('Cuartenario'), ft.dropdown.Option('Octal'), ft.dropdown.Option('Decimal'), ft.dropdown.Option('Hexadecimal')],)
    click2 = ElevatedButton(text='random')
    click = ElevatedButton(text='Transformar')
    fila_boton_click = Row([click, click2])
    fila_boton_click.alignment = 'center'
    
    
    fila_textf = Row([numero, resultado])
    fila_textf.alignment = 'center'
    fila_dropdown = Row([down_1, down_2])
    fila_dropdown.spacing = 50
    fila_dropdown.alignment = 'center'
    
    def btn_click(event):
        n = numero.value  # n es una cadena
        solucion = 'a'
            #Pasamos todo a decimales dependiendo del dropdown menu
        try:
            n = numero.value  # n es una cadena
            #Pasamos todo a decimales dependiendo del dropdown menu
            if down_1.value == "Decimal":
                decimal = decim(n, 10)
                if down_2.value == "Decimal":
                    solucion = str(decimal.getDecimal())
                elif down_2.value == "Binario":
                    solucion = str(binario(decimal.getDecimal()))
                elif down_2.value == "Cuartenario":
                    cuarte = cuart(decimal.getDecimal())
                    solucion = str(cuarte.getCuart())
                elif down_2.value == "Octal":
                    octal = octales(decimal.getDecimal())
                    solucion = str(octal.getOctal())
                elif down_2.value == "Ternario":
                    tern = ternario(decimal.getDecimal())
                    solucion = str(tern.getTer())
                elif down_2.value == "Hexadecimal":
                    hexa = hexas(decimal.getDecimal())
                    solucion = str(hexa.getHexa())
            
            if down_1.value == "Binario":
                decimal = decim(n, 2)
                if down_2.value == "Decimal":
                    solucion = str(decimal.getDecimal())
                elif down_2.value == "Binario":
                    solucion = str(binario(decimal.getDecimal()))
                elif down_2.value == "Cuartenario":
                    cuarte = cuart(decimal.getDecimal())
                    solucion = str(cuarte.getCuart())
                elif down_2.value == "Octal":
                    octal = octales(decimal.getDecimal())
                    solucion = str(octal.getOctal())
                elif down_2.value == "Ternario":
                    tern = ternario(decimal.getDecimal())
                    solucion = str(tern.getTer())
                elif down_2.value == "Hexadecimal":
                    hexa = hexas(decimal.getDecimal())
                    solucion = str(hexa.getHexa())
            
            if down_1.value == "Cuartenario":
                decimal = decim(n, 4)
                if down_2.value == "Decimal":
                    solucion = str(decimal.getDecimal())
                elif down_2.value == "Binario":
                    solucion = str(binario(decimal.getDecimal()))
                elif down_2.value == "Cuartenario":
                    cuarte = cuart(decimal.getDecimal())
                    solucion = str(cuarte.getCuart())
                elif down_2.value == "Octal":
                    octal = octales(decimal.getDecimal())
                    solucion = str(octal.getOctal())
                elif down_2.value == "Ternario":
                    tern = ternario(decimal.getDecimal())
                    solucion = str(tern.getTer())
                elif down_2.value == "Hexadecimal":
                    hexa = hexas(decimal.getDecimal())
                    solucion = str(hexa.getHexa())
            
            if down_1.value == "Octal":
                decimal = decim(n, 8)
                if down_2.value == "Decimal":
                    solucion = str(decimal.getDecimal())
                elif down_2.value == "Binario":
                    solucion = str(binario(decimal.getDecimal()))
                elif down_2.value == "Cuartenario":
                    cuarte = cuart(decimal.getDecimal())
                    solucion = str(cuarte.getCuart())
                elif down_2.value == "Octal":
                    octal = octales(decimal.getDecimal())
                    solucion = str(octal.getOctal())
                elif down_2.value == "Ternario":
                    tern = ternario(decimal.getDecimal())
                    solucion = str(tern.getTer())
                elif down_2.value == "Hexadecimal":
                    hexa = hexas(decimal.getDecimal())
                    solucion = str(hexa.getHexa())
            
            if down_1.value == "Ternario":
                decimal = decim(n, 3)
                if down_2.value == "Decimal":
                    solucion = str(decimal.getDecimal())
                elif down_2.value == "Binario":
                    solucion = str(binario(decimal.getDecimal()))
                elif down_2.value == "Cuartenario":
                    cuarte = cuart(decimal.getDecimal())
                    solucion = str(cuarte.getCuart())
                elif down_2.value == "Octal":
                    octal = octales(decimal.getDecimal())
                    solucion = str(octal.getOctal())
                elif down_2.value == "Ternario":
                    tern = ternario(decimal.getDecimal())
                    solucion = str(tern.getTer())
                elif down_2.value == "Hexadecimal":
                    hexa = hexas(decimal.getDecimal())
                    solucion = str(hexa.getHexa())
                    
            if down_1.value == "Hexadecimal":
                decimal = decim(n, 16)
                if down_2.value == "Decimal":
                    solucion = str(decimal.getDecimal())
                elif down_2.value == "Binario":
                    solucion = str(binario(decimal.getDecimal()))
                elif down_2.value == "Cuartenario":
                    cuarte = cuart(decimal.getDecimal())
                    solucion = str(cuarte.getCuart())
                elif down_2.value == "Octal":
                    octal = octales(decimal.getDecimal())
                    solucion = str(octal.getOctal())
                elif down_2.value == "Ternario":
                    tern = ternario(decimal.getDecimal())
                    solucion = str(tern.getTer())
                elif down_2.value == "Hexadecimal":
                    hexa = hexas(decimal.getDecimal())
                    solucion = str(hexa.getHexa())
                
            resultado.value = solucion
            page.update()
        except:
            resultado.value = 'Ingrese un numero valido'
    def btn_click2(event):
        try:
            valor = down_1.value
            numero.value = randomnum(valor)
            page.update()
        except:
            resultado.value = "Elegir opciones en los dropdown"
        
    click.on_click = btn_click
    click2.on_click = btn_click2
    page.add( fila_textf, fila_dropdown,  fila_boton_click)

def randomnum(value):
        if value == "Binario":
            c = "".join(str(random.randint(0, 1)) for i in range(random.randint(2, 3)))
        elif value == "Decimal":
            c = str(random.uniform(0,100))
        elif value == "Ternario":
            c = "".join(str(random.randint(0, 2)) for i in range(random.randint(2, 3)))
        elif value == "Cuartenario":
            c = "".join(str(random.randint(0, 3)) for i in range(random.randint(1, 2)))
        elif value == "Octal":
            c = "".join(str(random.randint(0, 7)) for i in range(random.randint(1, 2)))
        elif value == "Hexadecimal":
            c = "".join(random.choice("0123456789ABCDEF") for i in range(random.randint(1, 2)))
        return c
class decim():
    def __init__(self, numero, sistema):
        self.numero = int(numero)
        self.deci = int(numero, sistema)
    def getDecimal(self):
        return self.deci

def binario(numero):
    n = bin(numero)[2:]
    return n
        
class hexas():
    def __init__(self, numero):
        self.hexa = hex(numero)[2:]
    def getHexa(self):
        return self.hexa
 
    
class octales():
    def __init__(self, numero):
        self.octa = oct(numero)[2:]
    def getOctal(self):
        return self.octa


class ternario():
    def __init__(self, numero):
        self.ter = np.base_repr(numero, base=3)
    def getTer(self):
        return self.ter


class cuart():
    def __init__(self, numero):
        self.cuart = np.base_repr(numero, base=4)
    def getCuart(self):
        return self.cuart
    