from gestionArticulos import *
from gestionCliente import *
from gestionProveedor import *
from baseDeDatos import *
from OpcMenu import *
from validaciones import *
from gestionVentas import *
import os
os.system("cls")

print(f'''
♦- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -♦
:          BIENVENIDO/A !!! AL  SISTEMA Y GESTIÓN DE ABASTECIMIENTO                 :
:                        SUPPLY TECHNOLOGY PLG. SA.                                 :
♦- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -♦
''')
print(input("\nPresione 'ENTER' para comenzar..."))

class GestionComercial (object):
    def __init__(self):
        self.menuGral = (f'''
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            --                      "Gestion interna"                      --
            -----------------------------------------------------------------
            --  1: Menu Proveedores                                        --
            --  2: Menu Clientes                                           --
            --  3: Menu Articulos                                          --
            --  4: Menu Ventas                                             --
            --  5: Salir del Sistema                                       --
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            ''')
        self.menuProv = (f'''
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            --                    "Menu Proveedores"                       --
            -----------------------------------------------------------------
            --  1: Alta Proveedor                                          --
            --  2: Baja Proveedor                                          --
            --  3: Modificacion Proveedor                                  --
            --  4: Pedido Proveedor                                        --
            --  5: Devolución Proveedor                                    --
            --  6: Salir                                                   --
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            ''')
        self.menuCli = (f'''
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            --                    "Menu Clientes"                          --
            -----------------------------------------------------------------
            --  1: Alta Clientes                                           --
            --  2: Baja Clientes                                           --
            --  3: Modificacion Clientes                                   --
            --  4: Salir                                                   --
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            ''')
        self.menuArt = (f'''
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            --                     "Menu Articulos"                        --
            -----------------------------------------------------------------
            --  1: Alta Articulos                                          --
            --  2: Baja Articulos                                          --
            --  3: Modificacion Articulos                                  --
            --  4: Ingreso de Articulo                                     --
            --  5: Ingreso de remito                                       --
            --  6: Listado de articulos Faltantes                          --
            --  7: Salir                                                   --
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            ''')
        self.VentaDirecta = (f'''
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            --                      "Menu Venta"                           --
            -----------------------------------------------------------------
            --  1: Facturación (A)-(B)                                     --
            --  2: Listado Ventas Realizadas                               --
            --  3: Salir                                                   -- 
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            ''')
        
        self.estadoIVa = (f'''
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            --                      "Estado de IVA"                        --
            -----------------------------------------------------------------
            --  1: Inscripto                                               --
            --  2: Excento                                                 --
            --  3: Final                                                   -- 
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            ''')
        self.menu = opcMenu()
        self.gestProv = GestionProveedor()
        self.gestArt = GestionArticulos()
        self.gestCli = GestionCliente()
        self.val = Validacion()
        self.base = BaseDeDatos()
        self.gestVentas = gestionVentas()
        self.base.inicializacionBase()


    def menuVentas(self):
        seleccion = self.menu.menuNum(self.VentaDirecta,3)
        if seleccion == 1:
            final = 0
            nuevoDNI = self.val.numero('DNI',1000000,99999999)
            agregarConsFinal = self.base.hacerConsulta('Clientes','DNI_Cli',nuevoDNI)
            if type(agregarConsFinal) == str:
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

                print("\n Ingreso de Artículo Requerido para la Venta\n")
                nuevoCodBarra = self.val.numero('Código de Barra',99999999999,999999999999)
                artVenta = self.base.hacerConsulta("Articulos","codigoBarra",nuevoCodBarra)
                if not type(artVenta) == str:
                    print(f'''\nVerifique el artículo a vender:
                    Código de barra_______: {artVenta[0]}
                    Nombre de artículo____: {artVenta[1]}
                    Categoría de artículo_: {artVenta[2]}
                    Precio de artículo____: {artVenta[3]}
        --------►   Cantidad disp. art.___: {artVenta[4]}
                    Cuit de proveedor_____: {artVenta[5]}
                    ''')
                else:
                    print("\nEl código de barra ingresado no corresponde a un articulo registrado.\Verifique el artículo antes de la venta.")     
                self.gestVentas.CliCompra(nuevoCodBarra,artVenta)
            else:
                os.system("cls")
                print("""\nEl DNI corresponde a un cliente ya registrado.""")

                print("\nIngreso de Artículo Requerido para la Venta:")
                nuevoCodBarra = self.val.numero('Código de Barra',99999999999,999999999999)
                artVenta = self.base.hacerConsulta("Articulos","codigoBarra",nuevoCodBarra)
                os.system("cls")
                if not type(artVenta) == str:
                    print(f'''\nVerifique el artículo a vender:
                    Código de barra_______: {artVenta[0]}
                    Nombre de artículo____: {artVenta[1]}
                    Categoría de artículo_: {artVenta[2]}
                    Precio de artículo____: {artVenta[3]}
        --------►   Cantidad disp. art.___: {artVenta[4]}
                    Cuit de proveedor_____: {artVenta[5]}
                    ''')
                    
                else:
                    os.system("cls")
                    print(input("\nEl código de barra ingresado no corresponde a un articulo registrado.\nVerifique el artículo antes de la venta. Presione 'ENTER' para continuar..."))
                    self.menuArticulos()

                self.gestVentas.ventaArticulos(nuevoDNI)
                self.gestVentas.CliCompra(nuevoCodBarra,nuevoDNI)







        if seleccion==2:
            
            mydb = mariadb.connect(
                host="127.0.0.1",
                user="root",
#            password="RootPassword123!",    # no le puse pass a mi base por el momento
                database = "Gestion_Comercial"
                )

            mycursor = mydb.cursor()
            mycursor.execute("SELECT Precio_TotalArt FROM Ventas")
            miResult = mycursor.fetchall()
            for ind in miResult:
                print(ind)
            


            print(miResult)

            print(input("ENTER"))
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM Ventas")
            myresultado = mycursor.fetchall()
            print(F'''
               __________________________________________
               |   VENTAS REGISTRADAS A LA ACTUALIDAD   |
               ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
               ♦ MONTO TOTAL DE VENTAS A LA FECHA''')
            for tablaLista in myresultado:
                print(tablaLista)
                
                print(f'''
               
               ******************************************

               ♦ FECHA FACTURA_____________: {tablaLista[1]}
               ♦ N° DE FACTURA_____________: {tablaLista[2]}
               ♦ CÓDIGO BARRA ART__________: {tablaLista[3]}
               ♦ NOMBRE DE ART_____________: {tablaLista[4]}
               ♦ CANT.VENDIDA.ART__________: {tablaLista[5]}
               ♦ MONTO TOTAL ART___________: {tablaLista[7]}
               ♦ DNI CLIENTE_______________: {tablaLista[6]}
               ♦ NOMBRE CLIENTE____________: {tablaLista[8]}
               ♦ APELLIDO CLIENTE__________: {tablaLista[9]}
               ♦ SITUACIÓN IVA_____________: {tablaLista[10]}

               ******************************************
               ''')

            listaRegistros = []
            registros= self.base.cantidadDeRegistros('Ventas')
            for registro in registros:
                listaRegistros.append(list(registro))
                tablaVentas = """\
                        ---------------------- Se muestra un límite de 100 registros ----------------------                           
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| COD.VTA.     FECHA FACT.      N°FACTURA         COD.BARRA        NOMBRE ART.       CANT.ART.          DNI CLI.       MONTO T.         NOM.CLI.            APELL.CLI.         SIT.IVA CLI. |   
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
{}                                                                                                                                                                                                                   
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+\
"""
                tablaVentas = (tablaVentas.format('\n'.join("| {0:^8} | {1:^12} | {2:^12} | {3:^15} | {4:^20} | {5:^10} | {6:^10} | {7:^10} | {8:^20}| {9:^20} | {10:^10} |".format(*fila)
                for fila in listaRegistros)))
                os.system("cls")
                print(tablaVentas)
                print(listaRegistros)
            print(input("ENTER"))







        if seleccion==3:
            print("\nSe salió del Menú Venta")


    def menuArticulos(self):
        seleccion = self.menu.menuNum(self.menuArt,7)
        if seleccion == 1:
            nuevoCodBarra = self.val.numero('Código de Barra',99999999999,999999999999)
            nuevoCuit = self.val.numero('CUIT',9999999999,99999999999)
            cuitExiste = self.base.hacerConsulta('Proveedores','CUIL_CUIT_Prov',nuevoCuit)
            artACrear = self.base.hacerConsulta("Articulos","codigoBarra",nuevoCodBarra)
            if type(artACrear) == str and not type(cuitExiste) == str:
                nuevoNom = self.val.string30('Nombre de artículo')
                nuevaCat = self.val.stringSinNum('Categoría')
                nuevoPrecio = self.val.precio('Precio',0.1,999999.99)
                nuevaCant = self.val.numero('número de existencias',1,999)
                nuevoArt = [nuevoCodBarra,nuevoNom,nuevaCat,nuevoPrecio,nuevaCant,nuevoCuit]
                self.gestArt.altaArt(nuevoArt[0],nuevoArt)
            elif type(cuitExiste) == str:
                print(input("""\nEl CUIT ingresado no corresponde a ningún proveedor registrado.
                    Genere el alta de proveedor y vuelva a ingrear el artículo.
                    Se derivará al Menú Proveedores. Presione 'ENTER' para continuar..."""))
                self.menuProveedores()
            else:
                print("\nEl código de barra ingresado ya corresponde a un articulo registrado.\nSe salió del menu de alta de artículos.")
        if seleccion == 2:
            nuevoCodBarra = self.val.numero('Código de Barra',99999999999,999999999999)
            artABorrar = self.base.hacerConsulta("Articulos","codigoBarra",nuevoCodBarra)
            if not type(artABorrar) == str:
                self.gestArt.bajaArt(nuevoCodBarra)
            else:
                print("\nEl codigo de barra ingresado no se encuentra registrado.")
        if seleccion == 3:
            printModiArt = ('''
                -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
                --                    "Modificación de Artículo"               --
                -----------------------------------------------------------------
                --  1: Modificar Codigo de Barra                               --
                --  2: Modificar Nombre                                        --
                --  3: Modificar Categoría                                     --
                --  4: Modificar precio                                        --
                --  5: Modificar Cantidad                                      --
                --  6: Modificar Todo                                          --
                --  7: Salir                                                   --
                -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
                ''')
            codBarra = self.val.numero('Código de Barra',99999999999,999999999999)
            artAMod = self.base.hacerConsulta("Articulos","codigoBarra",codBarra)
            if not type(artAMod) == str:
                subMenu = self.menu.menuNum(printModiArt,7)
                if subMenu == 1:
                    nuevoCodBarra = self.val.numero('Nuevo Código de Barra',99999999999,999999999999)
                    artAMod[0] = nuevoCodBarra
                    self.gestArt.modificacionArt(codBarra,artAMod[0:5])
                if subMenu == 2:
                    nuevoNom = self.val.string30('Nuevo Nombre de artículo')
                    artAMod[1] = nuevoNom
                    self.gestArt.modificacionArt(codBarra,artAMod[0:5])
                if subMenu == 3:
                    nuevaCat = self.val.stringSinNum('Nueva Categoría')
                    artAMod[2] = nuevaCat
                    self.gestArt.modificacionArt(codBarra,artAMod[0:5])
                if subMenu == 4:
                    nuevoPrecio = self.val.precio('Nuevo Precio',0.1,999999.99)
                    artAMod[3] = nuevoPrecio
                    self.gestArt.modificacionArt(codBarra,artAMod[0:5])
                if subMenu == 5:
                    nuevaCant = self.val.numero('número de existencias',0,999)
                    artAMod[4] = nuevaCant
                    self.gestArt.modificacionArt(codBarra,artAMod[0:5])
                if subMenu == 6:
                    nuevoCodBarra = self.val.numero('Nuevo Código de Barra',99999999999,999999999999)
                    nuevoNom = self.val.string30('Nuevo Nombre de artículo')
                    nuevaCat = self.val.stringSinNum('Nueva Categoría')
                    nuevoPrecio = self.val.precio('Nuevo Precio',0.1,999999.99)
                    nuevaCant = self.val.numero('número de existencias',1,999)
                    articuloModi = [nuevoCodBarra,nuevoNom,nuevaCat,nuevoPrecio,nuevaCant]
                    self.gestArt.modificacionArt(codBarra,articuloModi)
                else:
                    pass
            else:
                print("\nEl código de barra ingresado ya corresponde a un articulo registrado.\nSe salió del menu de alta de artículos.")
        if seleccion == 4:
            nuevoCodBarra = self.val.numero('Código de Barra',99999999999,999999999999)
            cantidadDeArt = self.val.numero('número de existencias a ingresar',1,999)
            artAIngresar = self.base.hacerConsulta("Articulos","codigoBarra",nuevoCodBarra)
            if not type(artAIngresar) == str:
                self.gestArt.ingresoArt(nuevoCodBarra,cantidadDeArt)
            else:
                print("\nEl código de barra ingresado no corresponde a un artículo registrado.")
        if seleccion == 5:
            artDistintos = self.val.numero('número de artículos distintos a ingresar',1,50)
            listaCodBarra = []
            listaCantidad = []
            for cant in range(0,artDistintos):
                os.system('cls')
                nuevoCodBarra = self.val.numero('Código de Barra',99999999999,999999999999)
                cantidadDeArt = self.val.numero('número de existencias correspondiente al codigo de barra que ingresó',1,999)
                listaCodBarra.append(nuevoCodBarra)
                listaCantidad.append(cantidadDeArt)
            self.gestArt.ingresoRemito(listaCodBarra,listaCantidad)
        if seleccion == 6:
            self.gestArt.listadoSinStock()
        if seleccion == 7:
            print("\nSe salió del menu de alta de artículos.")
    def menuProveedores(self):
        seleccion = self.menu.menuNum(self.menuProv,6)
        if seleccion == 1:
            nuevoCuit= self.val.numero('CUIT',9999999999,99999999999)
            proveedorACrear = self.base.hacerConsulta("Proveedores","CUIL_CUIT_Prov",nuevoCuit)
            if type(proveedorACrear) == str:  
                nuevoNom = self.val.stringSinNum('Nombre de Proveedor')
                nuevaDir = self.val.string30('la dirección del proveedor')
                nuevoTel = self.val.numero('Teléfono',1099999999,11099999999)
                nuevoEmail = self.val.email()
                selIVA = self.menu.menuSel(self.estadoIVa,3)
                if selIVA == 1:
                    nuevoEstadoIva = 'Inscripto'
                elif selIVA == 2:
                    nuevoEstadoIva = 'Exento'
                else:
                    nuevoEstadoIva = 'Final'
                nuevoProv =[nuevoCuit,nuevoNom,nuevaDir,nuevoTel,nuevoEmail,nuevoEstadoIva]
                self.gestProv.altaProv(nuevoCuit,nuevoProv)
            else:
                os.system("cls")
                print("""\nEl CUIT corresponde a un proveedor ya registrado.""")
        if seleccion == 2:
            nuevoCuit= self.val.numero('CUIT',9999999999,99999999999)
            self.gestProv.bajaProv(nuevoCuit)
        if seleccion == 3:
            printModiProv = ('''
                -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
                --                 "Modificación de Proveedor"                 --
                -----------------------------------------------------------------
                --  1: Modificar CUIT                                          --
                --  2: Modificar Nombre                                        --
                --  3: Modificar Dirección                                     --
                --  4: Modificar Teléfono                                      --
                --  5: Modificar Email                                         --
                --  6: Modificar Estado de IVA                                 --
                --  7: Modificar Todo                                          --
                --  8: Salir                                                   --
                -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
                ''')
            provCuit= self.val.numero('CUIT',9999999999,99999999999)
            proveedorAMod = self.base.hacerConsulta("Proveedores","CUIL_CUIT_Prov",provCuit)
            if not type(proveedorAMod) == str:  
                subMenu = self.menu.menuNum(printModiProv,8)
                if subMenu == 1:
                    nuevoCuit = self.val.numero('Nuevo CUIT',9999999999,99999999999)
                    proveedorAMod[0] = nuevoCuit
                    self.gestProv.modificarProv(provCuit,proveedorAMod)
                if subMenu == 2:
                    nuevoNom = self.val.stringSinNum('Nuevo Nombre del Proveedor')
                    proveedorAMod[1] = nuevoNom
                    self.gestProv.modificarProv(provCuit,proveedorAMod)
                if subMenu == 3:
                    nuevaDir = self.val.string30('la nueva dirección del proveedor')
                    proveedorAMod[2] = nuevaDir
                    self.gestProv.modificarProv(provCuit,proveedorAMod)
                if subMenu == 4:
                    nuevoTel = self.val.numero('Nuevo Teléfono',1099999999,11099999999)
                    proveedorAMod[3] = nuevoTel
                    self.gestProv.modificarProv(provCuit,proveedorAMod)
                if subMenu == 5:
                    nuevoEmail = self.val.email()
                    proveedorAMod[4] = nuevoEmail
                    self.gestProv.modificarProv(provCuit,proveedorAMod)
                if subMenu == 6:
                    selIVA = self.menu.menuSel(self.estadoIVa,3)
                    if selIVA == 1:
                        nuevoEstadoIva = 'Inscripto'
                    elif selIVA == 2:
                        nuevoEstadoIva = 'Exento'
                    else:
                        nuevoEstadoIva = 'Final'
                    proveedorAMod[5] = nuevoEstadoIva
                    self.gestProv.modificarProv(provCuit,proveedorAMod)
                if subMenu == 7:
                    nuevoCuit = self.val.numero('Nuevo CUIT',9999999999,99999999999)
                    nuevoNom = self.val.stringSinNum('Nuevo Nombre del Proveedor')
                    nuevaDir = self.val.string30('la nueva dirección del proveedor')
                    nuevoTel = self.val.numero('Nuevo Teléfono',1099999999,11099999999)
                    nuevoEmail = self.val.email()
                    nuevoEstadoIva = self.val.stringSinNum('Estado de iva')
                    nuevoProv = [nuevoCuit,nuevoNom,nuevaDir,nuevoTel,nuevoEmail,nuevoEstadoIva]
                    self.gestProv.modificarProv(provCuit,nuevoProv)
                else:
                    os.system("cls")
                    print("\nSe salió del menu de modificación de proveedor.")
            else:
                os.system("cls")
                print("\nEl CUIT ingresado no corresponde a un proveedor registrado.")
        if seleccion == 4:
            pedidoCodBarra = self.val.numero('Código de barra',99999999999,999999999999)
            artASolicitar = self.base.hacerConsulta("Articulos","codigoBarra",pedidoCodBarra)
            if not type(artASolicitar) == str:
                pedidoCantidad = self.val.numero('Cantidad',1,1000)
                pedidoFecha = self.val.fecha()
                nuevoPedido=[pedidoCodBarra,pedidoCantidad,artASolicitar[1],pedidoFecha,artASolicitar[5]]
                self.gestProv.pedidoProveedor(nuevoPedido)
            else:
                os.system("cls")
                print("\nEl articulo solicitado no esta registrado en la base de datos. Genere el alta primero.")
        if seleccion == 5:
            devolucionCodBarra = self.val.numero('Código de barra del artículo a devolver',99999999999,999999999999)
            existeArt = self.base.hacerConsulta('Articulos','codigoBarra',devolucionCodBarra)
            if not type(existeArt) == str:
                devolucionCantidad = self.val.numero('Cantidad del artículo a devolver',1,1000)
                devolucionMotivo = self.val.stringSinNum('Motivo de la devolución')
                devolucionFecha = self.val.fecha()
                nuevaDevolucion = [devolucionCodBarra,devolucionCantidad,existeArt[5],devolucionMotivo,devolucionFecha]
                self.gestProv.devolucionProveedor(nuevaDevolucion)
            else:
                print("\nEl artículo que se intenta devolver no está registrado en la base de datos.")
        else:
            self.menuGeneral()
            
    def menuClientes(self):
        seleccion = self.menu.menuNum(self.menuCli,4)
        if seleccion == 1:
            nuevoDNI = self.val.numero('DNI',1000000,99999999)
            clienteACrear = self.base.hacerConsulta("Clientes","DNI_Cli",nuevoDNI)
            if type(clienteACrear) == str:   
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
            else:
                print("""\nEl DNI corresponde a un cliente ya registrado.""")
        if seleccion == 2:
            dniCliente = self.val.numero('DNI',1000000,99999999)
            self.gestCli.borrarCliente(dniCliente)
        if seleccion == 3:
            os.system("cls")
            printModiCli=(f'''
                -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
                --                    "Modificación de Cliente"                --
                -----------------------------------------------------------------
                --  1: Modificar DNI                                           --
                --  2: Modificar Nombre                                        --
                --  3: Modificar Apellido                                      --
                --  4: Modificar Dirección                                     --
                --  5: Modificar Teléfono                                      --
                --  6: Modificar Email                                         --
                --  7: Modificar Estado de IVA                                 --
                --  8: Modificar Todo                                          --
                --  9: Salir                                                   --
                -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
                ''')
            dniCliente = self.val.numero('DNI',1000000,99999999)
            cliente = self.base.hacerConsulta("Clientes","DNI_Cli",dniCliente)
            if not type(cliente) == str:
                subMenu = self.menu.menuNum(printModiCli,9)
                if subMenu == 1:
                    nuevoDNI = self.val.numero('Nuevo DNI',1000000,99999999)
                    cliente[0] = nuevoDNI
                    self.gestCli.modiClientes(dniCliente,cliente)
                if subMenu == 2:
                    nuevoNom = self.val.stringSinNum('Nuevo Nombre del cliente')
                    cliente[1] = nuevoNom
                    self.gestCli.modiClientes(dniCliente,cliente)
                if subMenu == 3:
                    nuevoApe = self.val.stringSinNum('Nuevo Apellido del cliente')
                    cliente[2] = nuevoApe
                    self.gestCli.modiClientes(dniCliente,cliente)
                if subMenu == 4:
                    nuevaDir = self.val.string30('la nueva dirección del cliente')
                    cliente[3] = nuevaDir
                    self.gestCli.modiClientes(dniCliente,cliente)
                if subMenu == 5:
                    nuevoTel = self.val.numero('Nuevo Teléfono',1099999999,11099999999)
                    cliente[4] = nuevoTel
                    self.gestCli.modiClientes(dniCliente,cliente)
                if subMenu == 6:
                    nuevoEmail = self.val.email()
                    cliente[5] = nuevoEmail
                    self.gestCli.modiClientes(dniCliente,cliente)
                if subMenu == 7:
                    selIVA = self.menu.menuSel(self.estadoIVa,3)
                    if selIVA == 1:
                        nuevoEstadoIva = 'Inscripto'
                    elif selIVA == 2:
                        nuevoEstadoIva = 'Exento'
                    else:
                        nuevoEstadoIva = 'Final'
                    cliente[6] = nuevoEstadoIva
                    self.gestCli.modiClientes(dniCliente,cliente)
                if subMenu == 8:
                    nuevoDNI = self.val.numero('Nuevo DNI',1000000,99999999)
                    nuevoNom = self.val.stringSinNum('Nuevo Nombre del cliente')
                    nuevoApe = self.val.stringSinNum('Nuevo Apellido del cliente')
                    nuevaDir = self.val.string30('la nueva dirección del cliente')
                    nuevoTel = self.val.numero('Nuevo Teléfono',1099999999,11099999999)
                    nuevoEmail = self.val.email()
                    nuevoEstadoIva = self.val.stringSinNum('Estado de iva')
                    nuevoCli = [nuevoDNI,nuevoNom,nuevoApe,nuevaDir,nuevoTel,nuevoEmail,nuevoEstadoIva]
                    self.gestCli.modiClientes(cliente[0],nuevoCli)
                else:
                    pass
            else:
                print("\nEl DNI ingresado no corresponde a un cliente registrado.\nSe salio del menu de modificación de cliente.")
        else:
            print("\nSe salió de: Menu Clientes.")            
    def menuGeneral(self):
        seleccion = self.menu.menuNum(self.menuGral,5)
        if seleccion == 1:
            self.menuProveedores()
        if seleccion == 2:
            self.menuClientes()
        if seleccion == 3:
            self.menuArticulos()
        if seleccion == 4:
            self.menuVentas()
        elif seleccion == 5:
            os.system("cls")
            print("\n        Cerrando el 'Sistema y Gestión de Abastecimiento'\n                 SUPPLY TECHNOLOGY PLG.SA.")
            print("\n\n...Programa Finalizado.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            exit()
    def menuLoop(self):
        validar=""
        while True:
            try:
                while validar!="NO":
                    self.menuGeneral()
                    self.base.inicializacionBase()
                    validar = input("\nDesea Realizar algo más? si/no: ").upper()
                    if validar!="SI" and validar!="NO":
                        print(f' Por favor ingrese Si o No.')
                    elif validar=="NO":
                        os.system("cls")
                        print("\n       Gracias por usar el 'Sistema y Gestión de Abastecimiento'\n              SUPPLY TECHNOLOGY PLG.SA.")
                        print("\n\n...Programa Finalizado.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                break
            except ValueError:
                print(f'Hubo un error en su ingreso.')

gestionCom = GestionComercial()
gestionCom.menuLoop()