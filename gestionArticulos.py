from baseDeDatos import BaseDeDatos
from opcMenu import *
import os

class GestionArticulos(object):
    def __init__(self):
        self.base = BaseDeDatos()
        self.base.inicializacionBase()
        self.menu = opcMenu()
        (f'''
        -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        --                    "Menu Articulos"                       --
        -----------------------------------------------------------------
        --  1: Alta Articulos --
        --  2: Baja Articulos --
        --  3: Modificacion Articulos --
        --  4: Ingreso de remito.--
        --  5: Listado de articulos --
        --  6: Salir. --
        -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        ''')
    def altaArt(self,articulo):
        print1 = (f'''Se va a generar el alta del articulo:
                    Código de barra: {articulo[0]}
                    Nombre de artículo: {articulo[1]}
                    Categoría de artículo: {articulo[2]}
                    Precio: {articulo[3]}
                    Cantidad: {articulo[4]}
                    Cuit de proveedor: {articulo[5]}''')
        if menu.menuSiNo(print1):
            os.system('cls')
            self.base.altaArticulo(articulo)
            print('\nRegistro exitoso.')
        else:
            print('\nSe canceló la operación.')




articulo = [125547888888,'MEMORIA RAM ASTRO 8GB','Memorias',2300.57,4,30234568879]

gesArt = GestionArticulos()
gesArt.altaArt(articulo)