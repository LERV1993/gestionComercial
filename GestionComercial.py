from gestionArticulos import *
from gestionCliente import *
from gestionProveedor import *
from baseDeDatos import *
from OpcMenu import *
from validaciones import *

class GestionComercial (object):
    def __init__(self):
        self.menuGral = (f'''
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            --                      "Gestion interna"                      --
            -----------------------------------------------------------------
            --  1: Menu Proveedores --
            --  2: Menu Clientes --
            --  3: Menu Articulos --
            --  4: Menu Ventas --
            --  5: Salir.--
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            ''')
        self.menuProv = (f'''
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            --                    "Menu Proveedores"                       --
            -----------------------------------------------------------------
            --  1: Alta Proveedor --
            --  2: Baja Proveedor --
            --  3: Modificacion Proveedor --
            --  4: Pedido Proveedor  --
            --  5: Devolución Proveedor  --
            --  6: Salir.--
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            ''')
        self.menuCli = (f'''
        -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        --                    "Menu Clientes"                          --
        -----------------------------------------------------------------
        --  1: Alta Clientes --
        --  2: Baja Clientes --
        --  3: Modificacion Clientes --
        --  4: Salir.--
        -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        ''')
        self.menuArt = (f'''
        -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        --                     "Menu Articulos"                        --
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
        self.menu = opcMenu()
        self.gestProv = GestionProveedor()
        self.gestArt = GestionArticulos()
        self.gestCli = GestionCliente()
        self.val = Validacion()
        self.base = BaseDeDatos()
        self.base.inicializacionBase()
    def menuProveedores(self):
        seleccion = self.menu.menuNum(self.menuProv,5)
        if seleccion == 1:
            nuevoCuit= self.val.numero('CUIT',9999999999,99999999999)
            proveedorACrear = self.base.hacerConsulta("Proveedores","CUIL_CUIT_Prov",nuevoCuit)
            if type(proveedorACrear) == str:  
                nuevoNom = self.val.stringSinNum('Nombre de Proveedor')
                nuevaDir = self.val.string30('la dirección del proveedor')
                nuevoTel = self.val.numero('Teléfono',1099999999,11099999999)
                nuevoEmail = self.val.email()
                nuevoEstadoIva = self.val.stringSinNum('Estado de iva')
                nuevoProv =[nuevoCuit,nuevoNom,nuevaDir,nuevoTel,nuevoEmail,nuevoEstadoIva]
                self.gestProv.altaProv(nuevoCuit,nuevoProv)
            else:
                print("""\nEl CUIT corresponde a un proveedor ya registrado.\nSe salió del menu de proveedores.""")
        if seleccion == 2:
            nuevoCuit= self.val.numero('CUIT',9999999999,99999999999)
            self.gestProv.bajaProv(nuevoCuit)
        if seleccion == 3:
            printModiProv = ('''
            -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
            --                    "Modificación de Cliente"                --
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
                seleccion = self.menu.menuNum(printModiProv,8)
                if seleccion == 1:
                    nuevoCuit = self.val.numero('Nuevo CUIT',9999999999,99999999999)
                    cuitViejo = proveedorAMod[0]
                    proveedorAMod[0] = nuevoCuit
                    self.gestProv.modificarProv(cuitViejo,proveedorAMod)
                if seleccion == 2:
                    nuevoNom = self.val.stringSinNum('Nuevo Nombre del Proveedor')
                    proveedorAMod[1] = nuevoNom
                    self.gestProv.modificarProv(proveedorAMod[0],proveedorAMod)
                if seleccion == 3:
                    nuevaDir = self.val.string30('la nueva dirección del proveedor')
                    proveedorAMod[2] = nuevaDir
                    self.gestProv.modificarProv(proveedorAMod[0],proveedorAMod)
                if seleccion == 4:
                    nuevoTel = self.val.numero('Nuevo Teléfono',1099999999,11099999999)
                    proveedorAMod[3] = nuevoTel
                    self.gestProv.modificarProv(proveedorAMod[0],proveedorAMod)
                if seleccion == 5:
                    nuevoEmail = self.val.email()
                    proveedorAMod[4] = nuevoEmail
                    self.gestProv.modificarProv(proveedorAMod[0],proveedorAMod)
                if seleccion == 6:
                    nuevoEstadoIva = self.val.stringSinNum('Estado de iva')
                    proveedorAMod[5] = nuevoEstadoIva
                    self.gestProv.modificarProv(proveedorAMod[0],proveedorAMod)
                if seleccion == 7:
                    nuevoCuit = self.val.numero('Nuevo CUIT',9999999999,99999999999)
                    nuevoNom = self.val.stringSinNum('Nuevo Nombre del Proveedor')
                    nuevaDir = self.val.string30('la nueva dirección del proveedor')
                    nuevoTel = self.val.numero('Nuevo Teléfono',1099999999,11099999999)
                    nuevoEmail = self.val.email()
                    nuevoEstadoIva = self.val.stringSinNum('Estado de iva')
                    nuevoProv = [nuevoCuit,nuevoNom,nuevaDir,nuevoTel,nuevoEmail,nuevoEstadoIva]
                    self.gestProv.modificarProv(proveedorAMod[0],nuevoProv)
                    print("\nSe salió del menu de modificación de proveedor.")
                else:
                    print("\nSe salió del menu de modificación de proveedor.")
            else:
                print("\nEl CUIT ingresado no corresponde a un proveedor registrado.\nSe salió del menu de modificación de proveedor. ")
        if seleccion == 4:
            pedidoCodBarra = self.val.numero('Código de barra',99999999999,999999999999)
            pedidoCantidad = self.val.numero('Cantidad',0,1000)
            pedidoNombre = self.val.string30('Articulo')
            pedidoFecha = self.val.fecha()
            pedidoCuit= self.val.numero('CUIT',9999999999,99999999999)
            nuevoPedido=[pedidoCodBarra,pedidoCantidad,pedidoNombre,pedidoFecha,pedidoCuit]
            self.gestProv.pedidoProveedor(nuevoPedido)
            print("\nSe salió del menu de proveedores.")
        if seleccion == 5:
            devolucionCodBarra = self.val.numero('Código de barra',99999999999,999999999999)
            devolucionCantidad = self.val.numero('Cantidad',0,1000)
            devolucionCuit= self.val.numero('CUIT',9999999999,99999999999)
            devolucionNombre = self.val.stringSinNum('Motivo')
            devolucionFecha = self.val.fecha()
            nuevaDevolucion = [devolucionCodBarra,devolucionCantidad,devolucionCuit,devolucionNombre,devolucionFecha]
            self.gestProv.devolucionProveedor(nuevaDevolucion)
            print("\nSe salió del menu de proveedores.")
        else:
            print("\nSe salió del menu de proveedores.")
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
                nuevoEstadoIva = self.val.stringSinNum('Estado de iva')
                nuevoCli = [nuevoDNI,nuevoNom,nuevoApe,nuevaDir,nuevoTel,nuevoEmail,nuevoEstadoIva]
                self.gestCli.altaCliente(nuevoDNI,nuevoCli)
            else:
                print("""\nEl DNI corresponde a un cliente ya registrado.\nSe salió del menu de clientes.""")
        if seleccion == 2:
            dniCliente = self.val.numero('DNI',1000000,99999999)
            self.gestCli.borrarCliente(dniCliente)
        if seleccion == 3:
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
                seleccion = self.menu.menuNum(printModiCli,9)
                if seleccion == 1:
                    nuevoDNI = self.val.numero('Nuevo DNI',1000000,99999999)
                    dniReg = cliente[0]
                    cliente[0] = nuevoDNI
                    self.gestCli.modiClientes(dniReg,cliente)
                if seleccion == 2:
                    nuevoNom = self.val.stringSinNum('Nuevo Nombre del cliente')
                    cliente[1] = nuevoNom
                    self.gestCli.modiClientes(dniReg,cliente)
                if seleccion == 3:
                    nuevoApe = self.val.stringSinNum('Nuevo Apellido del cliente')
                    cliente[2] = nuevoApe
                    self.gestCli.modiClientes(dniReg,cliente)
                if seleccion == 4:
                    nuevaDir = self.val.string30('la nueva dirección del cliente')
                    cliente[3] = nuevaDir
                    self.gestCli.modiClientes(dniReg,cliente)
                if seleccion == 5:
                    nuevoTel = self.val.numero('Nuevo Teléfono',1099999999,11099999999)
                    cliente[4] = nuevoTel
                    self.gestCli.modiClientes(dniReg,cliente)
                if seleccion == 6:
                    nuevoEmail = self.val.email()
                    cliente[5] = nuevoEmail
                    self.gestCli.modiClientes(dniReg,cliente)
                if seleccion == 7:
                    nuevoEstadoIva = self.val.stringSinNum('Estado de iva')
                    cliente[6] = nuevoEstadoIva
                    self.gestCli.modiClientes(dniReg,cliente)
                if seleccion == 8:
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
                    os.system('cls')
                    print("\nSe salió del menu de modificación de cliente.")
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
            print("\nOpción no disponible.")
        else:
            print("\nSe salió del menu general.")