import flet as ft
from calculadora import decim, traductor, hexas, octales, ternario, cuart, binario
from flet import Page, TextField, Dropdown, ElevatedButton, Row, Text
from gauss import Gausito, ElpanitaGauss

def main(page: Page):
    def si(event):
        page.clean()
        page.add(btn_r)
        traductor(page)
    def si2(event):
        page.clean()
        page.add(btn_r)
        Gausito(page)
    
    def regresar(event):
        page.clean()
        page.add(btn_r, fila_boton_click, Row(alignment=ft.MainAxisAlignment.CENTER, width=70, height=80) , fila_boton_click2)    
    
    
    page.bgcolor = "#009999"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    click = ElevatedButton(text='Conversiones', scale=2, on_click=si)
    fila_boton_click = Row([click])
    fila_boton_click.alignment = 'center'
    
    click2 = ElevatedButton(text='el pana Gaussito',  scale=2, on_click=si2)
    fila_boton_click2 = Row([click2])
    fila_boton_click2.alignment = 'center'
    
    btn_regresar = ElevatedButton(text = 'regresar', scale=2, on_click=regresar)
    btn_r = Row([btn_regresar])
    btn_r.alignment = 'start'
    page.add(btn_r, fila_boton_click, Row(alignment=ft.MainAxisAlignment.CENTER, width=70, height=80) , fila_boton_click2)
ft.app(target=main)