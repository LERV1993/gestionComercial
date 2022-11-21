from baseDeDatos import BaseDeDatos
from OpcMenu import *
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
        --  4: Ingreso de Articulo --
        --  5: Ingreso de remito.--
        --  6: Listado de articulos --
        --  7: Salir. --
        -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        ''')
    def altaArt(self,codBarra,articulo):
        artAGenerar = self.base.hacerConsulta('Articulos','codigoBarra',codBarra)
        if  type(artAGenerar) == str:
            print1 = (f'''Se va a generar el alta del artículo:
                        Código de barra: {articulo[0]}
                        Nombre de artículo: {articulo[1]}
                        Categoría de artículo: {articulo[2]}
                        Precio: {articulo[3]}
                        Cantidad: {articulo[4]}
                        Cuit de proveedor: {articulo[5]}''')
            if self.menu.menuSiNo(print1):
                os.system('cls')
                self.base.altaArticulo(articulo)
                print('\nRegistro exitoso.')
            else:
                print('\nSe canceló la operación.')
        else:
            print('\nEl artículo que se quiere dar de alta ya está registrado.')
    def bajaArt(self,codigoDeBarra):
        artABorrar = self.base.hacerConsulta('Articulos','codigoBarra',codigoDeBarra)
        if  not type(artABorrar) == str:
            print1 = (f'''Se va a eliminar el articulo:
                    Código de barra: {artABorrar[0]}
                    Nombre de artículo: {artABorrar[1]}
                    Categoría de artículo: {artABorrar[2]}
                    Precio: {artABorrar[3]}
                    Cantidad: {artABorrar[4]}
                    Cuit de proveedor: {artABorrar[5]}''')
            if self.menu.menuSiNo(print1):
                os.system('cls')
                self.base.borrarRegistro('Articulos','codigoBarra',codigoDeBarra)
                print('\nBorrado exitoso.')
            else:
                print('\nOperación cancelada.')
        else:
            print('\nEl codigo de barra ingresado no se encuentra registrado.')
    def modificacionArt(self,codBarra,artModificado):
        artAModificar = self.base.hacerConsulta('Articulos','codigoBarra',codBarra)
        if  not type(artAModificar) == str:
            print1 = (f'''Verifique los campos modificados del articulo:
                        Código de barra:  {artModificado[0]}
                        Nombre de artículo:  {artModificado[1]}
                        Categoría de artículo: {artModificado[2]}
                        Precio: {artModificado[3]}
                        Cantidad: {artModificado[4]}
                        Cuit de proveedor: {artAModificar[5]}''')
            if self.menu.menuSiNo(print1):
                os.system('cls')
                self.base.modificarArticulo(codBarra,artModificado)
                print('\nModificación exitosa.')
            else:
                print('\nOperación cancelada.')
        else:
            print('\nEl codigo de barra ingresado no se encuentra registrado.')
    def ingresoArt(self,codBarra,cantidad):
        ingreso = self.base.hacerConsulta('Articulos','codigoBarra',codBarra)
        if  not type(ingreso) == str:
            self.base.ingresarArticulos(codBarra,cantidad)
            print('\nIngreso exitoso.')
        else:
            print("\nEl código de barra ingresado no se encuentra registrado, genere el alta del articulo y vuelva a intentarlo.")
    def ingresoRemito(self,listaArticulos,listaCantidades):
        for ind in range(0,len(listaArticulos)):
            self.ingresoArt(listaArticulos[ind],listaCantidades[ind])
        #---------------------EJEMPLOS --------------------------------
        #articulos = [125547888888,825547877778,725547866666]
        #cantidades = [10,15,20]
    def listadoArt(self):
        listaRegistros = []
        registros= self.base.cantidadDeRegistros('Articulos')
        for registro in registros:
            listaRegistros.append(list(registro))
        tablaArticulos = """\
                        ---------------------- Se muestra un limite de 100 registros ----------------------                           
+-----------------------------------------------------------------------------------------------------------------------------------+
|   CODIGO DE BARRA               NOMBRE                  CATEGORIA        PRECIO        CANTIDAD            CUIT-PROVEEDOR         |   
|-----------------------------------------------------------------------------------------------------------------------------------|
{}
+-----------------------------------------------------------------------------------------------------------------------------------+\
"""
        tablaArticulos = (tablaArticulos.format('\n'.join("| {0:^18} |{1:^30} |{2:^15} |{3:^15}| {4:^10} | {5:^30} |".format(*fila)
 for fila in listaRegistros)))
        os.system('cls')
        print(tablaArticulos)