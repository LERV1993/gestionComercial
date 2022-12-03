from baseDeDatos import BaseDeDatos
from OpcMenu import *
from validaciones import *
from gestionCliente import *
import os

class gestionVentas(object):
    
    def __init__(self):
        self.base = BaseDeDatos()
        self.base.inicializacionBase()
        self.menu = opcMenu()
        self.val = Validacion()
        self.gestCli = GestionCliente()
        self.estadoIVa = (f'''
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            --                      "Estado de IVA"                        --
            -----------------------------------------------------------------
            --  1: Inscripto                                               --
            --  2: Excento                                                 --
            --  3: Final                                                   -- 
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            ''')
    def ventaArticulos(self,nuevoDNI):
        nuevoCli = self.base.hacerConsulta("Clientes","DNI_Cli",nuevoDNI)  
        if not type(nuevoCli) == str:
            
            print1=(f'''Registro de Comprador:
                DNI de cliente______: {nuevoCli[0]}
                Nombre de cliente___: {nuevoCli[1]}
                Apellido cliente____: {nuevoCli[2]}
                Direccion cliente___: {nuevoCli[3]}
                Telefono cliente____: {nuevoCli[4]}
                Email de cliente____: {nuevoCli[5]}
                Situación IVA cli___: {nuevoCli[6]}
                ''')
            print(print1)
            
        else:
            print("Nuevo cliente a registrar: ")
            nuevoNom = self.val.stringSinNum('Nombre del cliente')
            nuevoApe = self.val.stringSinNum('Apellido del cliente')
            nuevaDir = self.val.string30('la dirección del cliente')
            nuevoTel = self.val.numero('Teléfono',1099999999,11099999999)
            nuevoEmail = self.val.email()
            selIVA = self.menu.menuSel(self.estadoIVa,3)
            if selIVA == 1:
                nuevoEstadoIva = 'Inscripto'
            elif selIVA == 2:
                nuevoEstadoIva = 'Exento'
            else:
                nuevoEstadoIva = 'Final'
            nuevoCli = [nuevoDNI,nuevoNom,nuevoApe,nuevaDir,nuevoTel,nuevoEmail,nuevoEstadoIva]
            self.gestCli.altaCliente(nuevoDNI,nuevoCli)

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
            print(input("\nCompra Exitosa.\nLos artículos ya fueron solicitados al sector Depósito(descontados en stock)\nPresione 'ENTER' para continuar..."))
            cliente=self.base.hacerConsulta('Clientes','DNI_Cli',dniCliente)
            
            menuFactura=(f'''
            ELIJA OPCIÓN DE FACTURA
            Recuerde que el cliente es "{cliente[6]}"
            ----------------------------------------------
            -    1: FACTURA (A)  ----►  Inscripto        -
            -    2: FACTURA (B)  ----►  Final / Exento   -
            ----------------------------------------------
            ''')
            seleccion = self.menu.menuNum(menuFactura,2)
            os.system("cls")
            if seleccion==1:
                print("\nINGRESE DATOS ADICIONALES PARA TERMINAR FACTURACIÓN\n")
                
                print("\nformato de solicitud fecha: año:0000 - mes:00 - día:00")
                fechaFactura=self.val.fecha()
                
                numeroFactura1= self.base.ultimaFactura()
                
                totalIva=total*21/100
                cutiCliente=input("\nIngrese CUIT de cliente: ")
                cliente=self.base.hacerConsulta('Clientes','DNI_Cli',dniCliente)
                os.system("cls")
                
                print(f'''
                                    ♦============================================================♦
                                                              N° {numeroFactura1}
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
                vendido=[fechaFactura,numeroFactura1,compra[0],compra[1],cantVenta,cliente[0],total,cliente[1],cliente[2],cliente[6]]
                self.base.registrarVenta(vendido)





            else:
                print("\nINGRESE DATOS ADICIONALES PARA TERMINAR FACTURACIÓN\n")
                cliente=self.base.hacerConsulta('Clientes','DNI_Cli',dniCliente)
                print("\nformato de solicitud fecha: año:0000 - mes:00 - día:00")
                fechaFactura=self.val.fecha()
                numeroFactura1= self.base.ultimaFactura()
                
                os.system("cls")
                print(f'''
                                    ==============================================================
                                                              N° {numeroFactura1}
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
                vendido=[fechaFactura,numeroFactura1,compra[0],compra[1],cantVenta,cliente[0],total,cliente[1],cliente[2],cliente[6]]
                self.base.registrarVenta(vendido)


        else:
            print("\nOperación cancelada.")
        
    def listadoVentas(self):
            listaRegistros = []
            registros= self.base.cantidadDeRegistros('Ventas')
            datos = []
            mlist = []
            for lista in range(0,len(registros)):
                for elemento in range(0,len(registros[lista])):
                    if elemento != 1 and elemento < 10:
                        mlist.append(registros[lista][elemento])
                    elif elemento == 1:
                        mlist.append(str(registros[lista][elemento]))
                    else:
                        mlist.append(str(registros[lista][elemento]))
                        datos.append(mlist)
                        mlist=[]
             
                    
            for registro in datos:
                listaRegistros.append(list(registro))
                tablaVentas = """\
                                                                     ---------------------- Se muestra un límite de 100 registros ----------------------                           
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   COD.VTA.       FECHA FACT.        N°FACTURA        COD.BARRA                NOMBRE ART              CANT.ART.     DNI CLI.    MONTO T.                NOM.CLI.                      APELL.CLI.            SIT.IVA CLI. |   
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
{}                                                                                                                                                                                                                   
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+\
"""
                tablaVentas = (tablaVentas.format('\n'.join("| {0:^10} | {1:^18} | {2:^12} | {3:^16} | {4:^30} | {5:^10} | {6:^10} | {7:^10} | {8:^30}| {9:^30} | {10:^11} |".format(*fila)
                for fila in listaRegistros)))
            print(tablaVentas)
    
