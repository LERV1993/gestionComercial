from baseDeDatos import BaseDeDatos
from OpcMenu import *
from validaciones import *
import os

class gestionVentas(object):
    
    def __init__(self):
        self.base = BaseDeDatos()
        self.base.inicializacionBase()
        self.menu = opcMenu()
        self.val = Validacion()

    def ventaArticulos(self,nuevoDNI):

        self.nuevoCli = self.base.hacerConsulta("Clientes","DNI_Cli",nuevoDNI)  
        if type(self.nuevoCli) == str:
            
            print1=(f'''Registro de Comprador:
                DNI de cliente______: {self.nuevoCli[0]}
                Nombre de cliente___: {self.nuevoCli[1]}
                Apellido cliente____: {self.nuevoCli[2]}
                Direccion cliente___: {self.nuevoCli[3]}
                Telefono cliente____: {self.nuevoCli[4]}
                Email de cliente____: {self.val.email()}
                Situación IVA cli___: {self.nuevoCli[6]}
                ''')
            print("ACA")
            print(print1)
            if self.menu.menuSiNo(print1):
                
                self.base.altaCliente(self.nuevoCli)
                print("\n Registro de cliente exitoso.")
            else:
                print("\nSe canceló la operación.")
        else:
            
            print2=(f'''Registro de Comprador:
                    DNI de cliente______: {self.nuevoCli[0]}
                    Nombre de cliente___: {self.nuevoCli[1]}
                    Apellido cliente____: {self.nuevoCli[2]}
                    Direccion cliente___: {self.nuevoCli[3]}
                    Telefono cliente____: {self.nuevoCli[4]}
                    Email de cliente____: {self.nuevoCli[5]}
                    Situación IVA cli___: {self.nuevoCli[6]}
                    ''')
            print(print2)

    def CliCompra(self,nuevoCodBarra,dniCliente):

        compra = self.base.hacerConsulta("Articulos","codigoBarra",nuevoCodBarra)
        print("Datos extraidos del sistema.\nVerifique información antes de generar cantidad solicitada por comprador.")
        cantVenta = int(input("\nIngrese cantidad de producto/s a vender: "))
        compra[4] = cantVenta
        total=compra[3] * cantVenta
        print2 = (f'''
        •-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•
             SE VENDIO...                                          
                      {cantVenta} unidades de {compra[1]}           
                                                                    
                                   Total Abonar $: {total}          
        •-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•-•
        ''')      
        if self.menu.menuSiNo(print2):
            self.base.descuentaArticulos(nuevoCodBarra,cantVenta)
            os.system("cls")
            print("\nCompra Exitosa.\nLos artículos ya fueron solicitados al sector Depósito(descontados en stock)\n")
            cliente=self.base.hacerConsulta('Clientes','DNI_Cli',dniCliente)
            print(f'''
            ELIJA OPCIÓN DE FACTURA
            Recuerda que el cliente es "{cliente[6]}"
            ----------------------------------------------
            -    1: FACTURA (A)  ----►  Inscripto        -
            -    2: FACTURA (B)  ----►  Final / Exento   -
            ----------------------------------------------
            ''')
            self.opc=int(input("Ingrese opción de comprobante: "))
            os.system("cls")
            if self.opc==1:
                print("\nINGRESE DATOS ADICIONALES PARA TERMINAR FACTURACIÓN\n")
                
                print("\nformato de solicitud fecha: año:0000 - mes:00 - día:00")
                fechaFactura=self.val.fecha()
                
                numeroFactura1="0001-000000"
                numeroFactura2=+1
                
                totalIva=total*21/100
                cutiCliente=input("\nIngrese CUIT de cliente: ")
                cliente=self.base.hacerConsulta('Clientes','DNI_Cli',dniCliente)
                os.system("cls")
                
                print(f'''
                                    ♦============================================================♦
                                                         N° {numeroFactura1}{numeroFactura2}
                                    ♦      ♦                  FACTURA (A)                 ♦      ♦
                                                                               Fecha: {fechaFactura}
                                    ♦============================================================♦
                                    ♦ tel: 011-5175-9042       EMPRESA: SUPPLY TECHNOLOGY PLG.SA ♦
                                    ♦      011-6522-1397       Cuit: 30-24769651-2               ♦
                                    ♦                          Dirección: Av.Corrientes 3492     ♦
                                    ♦============================================================♦
                                    Cliente Inscripto (Cuit: {cutiCliente})                   
                                    --------------------------------------------------------------

                                    Nombre Cliente                         {cliente[1]}
                                    Dirección Cliente                      {cliente[3]}
                                    Estado IVA Cliente                     {cliente[6]}
                                    DNI del Cliente                        {cliente[0]}           


                                    ==============================================================
                                    -  ARTICULO/S                                                -
                                    --------------------------------------------------------------

                                    Código de Artículo                     {compra[0]}
                                    Nombre de Artículo                     {compra[1]}
                                    Unidades de Artículo                   {cantVenta}
                                    Precio Unitario                      $ {compra[3]}


                                    ♦============================================================♦ 
                                    Montos de compra__SubTotal__Iva 21%  $ {totalIva}
                                                      Total______________$ {total}     
                                    ♦============================================================♦
                                                ''')
                vendido=[fechaFactura,numeroFactura2,compra[0],compra[1],cantVenta,total,cliente[0],cliente[1],cliente[2],cliente[6]]
                self.base.registrarVenta(vendido)




            else:
                print("\nINGRESE DATOS ADICIONALES PARA TERMINAR FACTURACIÓN\n")
                cliente=self.base.hacerConsulta('Clientes','DNI_Cli',dniCliente)
                print("\nformato de solicitud fecha: año:0000 - mes:00 - día:00")
                fechaFactura=self.val.fecha()
                
                numeroFactura1="0001-000000"
                numeroFactura2=+1
                
                os.system("cls")
                print(f'''
                                    ==============================================================
                                                         N° {numeroFactura1}{numeroFactura2}
                                    -      ♦                  FACTURA (B)                 ♦      -
                                                                           Fecha: {fechaFactura}
                                    ==============================================================
                                    - tel: 011-5175-9042       EMPRESA: SUPPLY TECHNOLOGY PLG.SA -
                                    -      011-6522-1397       Cuit: 30-24769651-2               -
                                    -                          Dirección: Av.Corrientes 3492     -
                                    ==============================================================
                                    -  Cliente Final/Exento                                      -
                                    ==============================================================

                                    Nombre Cliente                         {cliente[1]}
                                    Dirección Cliente                      {cliente[3]}
                                    Estado IVA Cliente                     {cliente[6]}
                                    DNI del Cliente                        {cliente[0]}       
                                    
                                    
                                    --------------------------------------------------------------
                                    -  ARTICULO/S                                                -
                                    --------------------------------------------------------------
                                    
                                    Código de Artículo                     {compra[0]}
                                    Nombre de Artículo                     {compra[1]}
                                    Unidades de Artículo                   {cantVenta}
                                    Precio Unitario                      $ {compra[3]}
                                    
                                    
                                    ==============================================================
                                    Montos de compra________Total________$ {total}     
                                    ==============================================================
                                                ''')
                vendido=[fechaFactura,numeroFactura2,compra[0],compra[1],cantVenta,total,cliente[0],cliente[1],cliente[2],cliente[6]]
                self.base.registrarVenta(vendido)


        else:
            print("\nOperación cancelada.")
        
    def listadoVentas(self,lista):
        lista=self.base.cantidadDeRegistros()
        print(lista)
    
