import numpy as np
import flet as ft
from flet import Page, TextField, Dropdown, ElevatedButton, Row, Text


def main(page: Page):
    def btn_click(event):
        try:
            n = numero.value  # n es una cadena
            if drop_lenguaje1.value == 'Decimal':
                n = int(n)  # convertir n a un entero
                if drop_lenguaje2.value == 'Binario':
                    resultado.value = decimal_bin(n)
                elif drop_lenguaje2.value == 'Ternario':
                    resultado.value = decimal_ternario(n)
                elif drop_lenguaje2.value == 'Cuartenario':
                    resultado.value = decimal_cuartenario(n)
                elif drop_lenguaje2.value == 'Octal':
                    resultado.value = decimal_octal(n)
                elif drop_lenguaje2.value == 'Decimal':
                    resultado.value = str(n)
                elif drop_lenguaje2.value == 'Hexadecimal':
                    resultado.value = decimal_hexadecimal(n)
            elif drop_lenguaje1.value == 'Binario':
                if drop_lenguaje2.value == 'Ternario':
                    resultado.value = bin_ternario(n)
                elif drop_lenguaje2.value == 'Cuartenario':
                    resultado.value = bin_cuartenario(n)
                elif drop_lenguaje2.value == 'Octal':
                    resultado.value = bin_octal(n)
                elif drop_lenguaje2.value == 'Decimal':
                    resultado.value = bin_decimal(n)
                elif drop_lenguaje2.value == 'Hexadecimal':
                    resultado.value = bin_hexadecimal(n)
            elif drop_lenguaje1.value == 'Ternario':
                if drop_lenguaje2.value == 'Binario':
                    resultado.value = ternario_bin(n)
                elif drop_lenguaje2.value == 'Ternario':
                    resultado.value = str(n)
                elif drop_lenguaje2.value == 'Cuartenario':
                    resultado.value = ternario_cuartenario(n)
                elif drop_lenguaje2.value == 'Octal':
                    resultado.value = ternario_octal(n)
                elif drop_lenguaje2.value == 'Decimal':
                    resultado.value = ternario_decimal(n)
                elif drop_lenguaje2.value == 'Hexadecimal':
                    resultado.value = ternario_hexadecimal(n)
            elif drop_lenguaje1.value == 'Cuartenario':
                if drop_lenguaje2.value == 'Binario':
                    resultado.value = cuartenario_bin(n)
                elif drop_lenguaje2.value == 'Ternario':
                    resultado.value = cuartenario_ternario(n)
                elif drop_lenguaje2.value == 'Cuartenario':
                    resultado.value = str(n)
                elif drop_lenguaje2.value == 'Octal':
                    resultado.value = cuartenario_octal(n)
                elif drop_lenguaje2.value == 'Decimal':
                    resultado.value = cuartenario_decimal(n)
                elif drop_lenguaje2.value == 'Hexadecimal':
                    resultado.value = cuartenario_hexadecimal(n)
            elif drop_lenguaje1.value == 'Octal':
                if drop_lenguaje2.value == 'Binario':
                    resultado.value = octal_bin(n)
                elif drop_lenguaje2.value == 'Ternario':
                    resultado.value = octal_ternario(n)
                elif drop_lenguaje2.value == 'Cuartenario':
                    resultado.value = octal_cuartenario(n)
                elif drop_lenguaje2.value == 'Octal':
                    resultado.value = str(n)
                elif drop_lenguaje2.value == 'Decimal':
                    resultado.value = octal_decimal(n)
                elif drop_lenguaje2.value == 'Hexadecimal':
                    resultado.value = octal_hexadecimal(n)
            elif drop_lenguaje1.value == 'Hexadecimal':
                if drop_lenguaje2.value == 'Binario':
                    resultado.value = hexadecimal_bin(n)
                elif drop_lenguaje2.value == 'Ternario':
                    resultado.value = hexadecimal_ternario(n)
                elif drop_lenguaje2.value == 'Cuartenario':
                    resultado.value = hexadecimal_cuartenario(n)
                elif drop_lenguaje2.value == 'Octal':
                    resultado.value = hexadecimal_octal(n)
                elif drop_lenguaje2.value == 'Decimal':
                    resultado.value = hexadecimal_decimal(n)
                elif drop_lenguaje2.value == 'Hexadecimal':
                    resultado.value = str(n)
            page.update()
        except:
            resultado.value = 'Ingrese un numero valido'
    page.title = 'Transformador DL'
    espacio_superior = Text(""" 




""")

    numero = TextField(label='Ingrese un numero')
    resultado = TextField(label='Resultado')
    drop_lenguaje1 = Dropdown(width=135, options=[ft.dropdown.Option('Binario'), ft.dropdown.Option(
        'Ternario'), ft.dropdown.Option('Cuartenario'), ft.dropdown.Option('Octal'), ft.dropdown.Option('Decimal'), ft.dropdown.Option('Hexadecimal')],)
    drop_lenguaje2 = Dropdown(width=135, options=[ft.dropdown.Option('Binario'), ft.dropdown.Option(
        'Ternario'), ft.dropdown.Option('Cuartenario'), ft.dropdown.Option('Octal'), ft.dropdown.Option('Decimal'), ft.dropdown.Option('Hexadecimal')],)
    click = ElevatedButton(text='Transformar', on_click=btn_click)
    fila_boton_click = Row([click])
    fila_boton_click.alignment = 'center'
    fila_textf = Row([numero, resultado])
    fila_textf.alignment = 'center'
    fila_dropdown = Row([drop_lenguaje1, drop_lenguaje2])
    fila_dropdown.spacing = 335
    fila_dropdown.alignment = 'center'

    page.add(espacio_superior, fila_textf, fila_dropdown,  fila_boton_click)


def decimal_bin(n):
    n = bin(n)[2:]
    return n


def decimal_ternario(n):
    return np.base_repr(n, base=3)


def decimal_cuartenario(n):
    return np.base_repr(n, base=4)


def decimal_octal(n):
    n = oct(n)[2:]
    return n


def decimal_hexadecimal(n):
    n = hex(n)[2:]
    return n


def bin_ternario(n):
    decimal = int(n, 2)
    n = np.base_repr(decimal, base=3)
    return n


def bin_cuartenario(n):
    decimal = int(n, 2)
    cuartenario = np.base_repr(decimal, base=4)
    return cuartenario


def bin_octal(n):
    decimal = int(n, 2)
    n = oct(decimal)[2:]
    return n


def bin_decimal(n):
    decimal = int(n, 2)
    return str(decimal)


def bin_hexadecimal(n):
    decimal = int(n, 2)
    hexadecimal = hex(decimal)[2:]
    return hexadecimal


def ternario_bin(n):
    decimal = int(n, 3)
    binario = bin(decimal)[2:]
    return binario


def ternario_cuartenario(n):
    decimal = int(n, 3)
    cuartenario = np.base_repr(decimal, base=4)
    return cuartenario


def ternario_octal(n):
    decimal = int(n, 3)
    octal = oct(decimal)[2:]
    return octal


def ternario_decimal(n):
    decimal = int(n, 3)
    return str(decimal)


def ternario_hexadecimal(n):
    decimal = int(n, 3)
    hexadecimal = hex(decimal)[2:]
    return hexadecimal


def cuartenario_bin(n):
    decimal = int(n, 4)
    binario = bin(decimal)[2:]
    return binario


def cuartenario_ternario(n):
    decimal = int(n, 4)
    ternario = np.base_repr(decimal, base=3)
    return ternario


def cuartenario_octal(n):
    decimal = int(n, 4)
    octal = oct(decimal)[2:]
    return octal


def cuartenario_decimal(n):
    decimal = int(n, 4)
    return str(decimal)


def cuartenario_hexadecimal(n):
    decimal = int(n, 4)
    hexadecimal = hex(decimal)[2:]
    return hexadecimal


def octal_bin(n):
    decimal = int(n, 8)
    binario = bin(decimal)[2:]
    return binario


def octal_ternario(n):
    decimal = int(n, 8)
    ternario = np.base_repr(decimal, base=3)
    return ternario


def octal_cuartenario(n):
    decimal = int(n, 8)
    octal = np.base_repr(decimal, base=4)
    return octal


def octal_decimal(n):
    decimal = int(n, 8)
    return str(decimal)


def octal_hexadecimal(n):
    decimal = int(n, 8)
    hexadecimal = hex(decimal)[2:]
    return hexadecimal


def hexadecimal_bin(n):
    decimal = int(n, 16)
    binario = bin(decimal)[2:]
    return binario


def hexadecimal_ternario(n):
    decimal = int(n, 16)
    ternario = np.base_repr(decimal, base=3)
    return ternario


def hexadecimal_cuartenario(n):
    decimal = int(n, 16)
    cuartenario = np.base_repr(decimal, base=4)
    return cuartenario


def hexadecimal_octal(n):
    decimal = int(n, 16)
    octal = oct(decimal)[2:]
    return octal


def hexadecimal_decimal(n):
    decimal = int(n, 16)
    return str(decimal)


ft.app(target=main)
