import numpy as np
import flet as ft
from flet import Page, TextField, Dropdown, ElevatedButton, Row, Text


def traductor(page: Page):
    page.title = 'Transformador DL'
    
    numero = TextField(label='Ingrese un numero')
    resultado = TextField(label='Resultado', value = 0)
    down_1 = Dropdown(width=135, options=[ft.dropdown.Option('Binario'), ft.dropdown.Option(
        'Ternario'), ft.dropdown.Option('Cuartenario'), ft.dropdown.Option('Octal'), ft.dropdown.Option('Decimal'), ft.dropdown.Option('Hexadecimal')],)
    down_2 = Dropdown(width=135, options=[ft.dropdown.Option('Binario'), ft.dropdown.Option(
        'Ternario'), ft.dropdown.Option('Cuartenario'), ft.dropdown.Option('Octal'), ft.dropdown.Option('Decimal'), ft.dropdown.Option('Hexadecimal')],)
    click = ElevatedButton(text='Transformar')
    fila_boton_click = Row([click])
    fila_boton_click.alignment = 'center'
    click2 = ElevatedButton(text='Transformar')
    fila_boton_click2 = Row([click])
    
    fila_textf = Row([numero, resultado])
    fila_textf.alignment = 'center'
    fila_dropdown = Row([down_1, down_2])
    fila_dropdown.spacing = 335
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


    click.on_click = btn_click
    page.add( fila_textf, fila_dropdown,  fila_boton_click, fila_boton_click2)

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
    