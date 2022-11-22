from gestionArticulos import *
from gestionCliente import *
from gestionProveedor import *
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
            --  4: Devolucion Proveedor  --
            --  5: Salir.--
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
        self.menuArticulos = (f'''
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
        #self.gestProv = GestionProveedores()
        self.gestArt = GestionArticulos()
        self.gestCli = GestionCliente()
        self.val = Validacion()
    def menuProveedores(self):
        seleccion = self.menu.menuNum(self.menuProv,5)
    def menuClientes(self):
        seleccion = self.menu.menuNum(self.menuCli,4)
        if seleccion == 1:
            nuevoDNI = self.val.numero('DNI',1000000,99999999)
            nuevoNom = self.val.stringSinNum('Nombre del cliente')
            nuevoApe = self.val.stringSinNum('Apellido del cliente')
            nuevaDir = self.val.string30('la dirección del cliente')
            nuevoTel = self.val.numero('Teléfono',1099999999,11099999999)
            nuevoEmail = self.val.string30('el email del cliente')
            nuevoEstadoIva = self.val.stringSinNum('Estado de iva')
            nuevoCli = [nuevoDNI,nuevoNom,nuevoApe,nuevaDir,nuevoTel,nuevoEmail,nuevoEstadoIva]
            self.gestCli.altaCliente(nuevoDNI,nuevoCli)
        if seleccion == 2:
            dniCliente = self.val.numero('DNI',1000000,99999999)
            self.gestCli.borrarCliente(dniCliente)
        if seleccion == 3:
            printModiCli=(f'''
        -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        --                    "Modificacio de Cliente"                 --
        -----------------------------------------------------------------
        --  1: Modificar DNI --
        --  2: Modificar Nombre --
        --  3: Modificar Apellido --
        --  4: Modificar Dirección --
        --  5: Modificar Teléfono --
        --  6: Modificar Email --
        --  7: Modificar Estado de IVA --
        --  8: Modificar Todo --
        --  9: Salir --
        -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        ''')
            dniCliente = self.val.numero('DNI',1000000,99999999)
            cliente = self.gestCli.traerCliente(dniCliente)
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
                    nuevoTel = self.val.numero('Teléfono',1099999999,11099999999)
                    cliente[4] = nuevoTel
                    self.gestCli.modiClientes(dniReg,cliente)
                if seleccion == 6:
                    nuevoEmail = self.val.string30('el email del cliente')
                    cliente[5] = nuevoEmail
                    self.gestCli.modiClientes(dniReg,cliente)
                if seleccion == 7:
                    nuevoEstadoIva = self.val.stringSinNum('Estado de iva')
                    cliente[6] = nuevoEstadoIva
                    self.gestCli.modiClientes(dniReg,cliente)
                if seleccion == 8:
                    nuevoDNI = self.val.numero('DNI',1000000,99999999)
                    nuevoNom = self.val.stringSinNum('Nombre del cliente')
                    nuevoApe = self.val.stringSinNum('Apellido del cliente')
                    nuevaDir = self.val.string30('la dirección del cliente')
                    nuevoTel = self.val.numero('Teléfono',1099999999,11099999999)
                    nuevoEmail = self.val.string30('el email del cliente')
                    nuevoEstadoIva = self.val.stringSinNum('Estado de iva')
                    nuevoCli = [nuevoDNI,nuevoNom,nuevoApe,nuevaDir,nuevoTel,nuevoEmail,nuevoEstadoIva]
                    self.gestCli.modiClientes(cliente[0],nuevoCli)
                else:
                    os.system('cls')
                    print("\nSe salió del menu de modificación de cliente.")
            else:
                print("\nEl DNI ingresado no corresponde a un cliente registrado.")
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

gesCom = GestionComercial()
gesCom.menuClientes()