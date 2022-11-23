from baseDeDatos import BaseDeDatos
from OpcMenu import *
import os
##   - Alta/Baja/Modificación de Proveedor (DNI, Nombre de Fantasía, Direccion, Telefono, mail, Situacion IVA (Inscripto, Exento, etc..))
##         - Pedido de reposición a Proveedor
##        - Devolución a proveedor: se podrá realizar una baja de stock de articulos de un proveedor para devolver, 
##         habrá que completar un campo Observacion o Estado(vencido, dañado, etc)


class GestionProveedor(object):
    def __init__(self):
        self.base = BaseDeDatos()
        self.base.inicializacionBase()
        self.menu = opcMenu()
    def altaProv(self,Prov,proveedor):
        IngresoProveedor=self.base.hacerConsulta('Proveedores','CUIL_CUIT_Prov',Prov)
        if type(IngresoProveedor)==str:
            print1 = (f'''Se va a generar el alta del proveedor:
                    CUIL / CUIT PROV.   : {proveedor[0]}
                    Nombre de Proveedor : {proveedor[1]}
                    Dirección Proveedor : {proveedor[2]}
                    Teléfono Proveedor  : {proveedor[3]}
                    Mail de Proveedor   : {proveedor[4]}
                    Estado IVA Proveedor: {proveedor[5]}
                    ''')
            if self.menu.menuSiNo(print1):
                os.system('cls')
                self.base.altaProveedor(proveedor)
                print('\nRegistro exitoso.\n')
            else:
                print('\nSe canceló la operación.\n')
        else:
            print("Proveedor ya registrado en Base de Datos...\n")
    def bajaProv(self,Prov):
        ingresoProveedor=self.base.hacerConsulta('Proveedores','CUIL_CUIT_Prov',Prov)
        if not type(ingresoProveedor)==str:
            print1 = (f'''\nSe va a generar la baja del proveedor:\n
                    CUIL / CUIT PROV.   : {ingresoProveedor[0]}
                    Nombre de Proveedor : {ingresoProveedor[1]}
                    Dirección Proveedor : {ingresoProveedor[2]}
                    Teléfono Proveedor  : {ingresoProveedor[3]}
                    Mail de Proveedor   : {ingresoProveedor[4]}
                    Estado IVA Proveedor: {ingresoProveedor[5]}
                    ''')
            if self.menu.menuSiNo(print1):
                os.system('cls')
                self.base.borrarRegistro('Proveedores','CUIL_CUIT_Prov',Prov)
                print('\nSe ha dado de baja a Proveedor.\n')
            else:
                print('\nSe canceló la operación.\n')
        else:
            print("Proveedor no registrado en Base de Datos.")
    def modificarProv(self,Prov,modprov):
        proveedorAMod=self.base.hacerConsulta('Proveedores','CUIL_CUIT_Prov',Prov)
        if not type(proveedorAMod)==str:
            print1 = (f'''\nSe va a Modificar los datos de proveedor:\n
                    CUIL / CUIT PROV.   : {modprov[0]}
                    Nombre de Proveedor : {modprov[1]}
                    Dirección Proveedor : {modprov[2]}
                    Teléfono Proveedor  : {modprov[3]}
                    Mail de Proveedor   : {modprov[4]}
                    Estado IVA Proveedor: {modprov[5]}
                    ''')
            if self.menu.menuSiNo(print1):
                os.system('cls')
                self.base.modificarProveedor(Prov,modprov)
                print('\nSe ha modificado los datos exitosamente.\n')
            else:
                print('\nSe canceló la operación.\n')
        else:
            print("CUIL/CUIT no registrado en Tabla Proveedores.")
    def pedidoProveedor(self,pedidoprov):
        print1 = (f'''\nSolicitud por OP. de:\n
                    Código de Barra     : {pedidoprov[0]}
                    Cantidad Artículo   : {pedidoprov[1]}
                    Nombre de Artículo  : {pedidoprov[2]}
                    Fecha de Solicitud  : {pedidoprov[3]}
                    CUIL/CUIT Proveedor : {pedidoprov[4]}
                    Estado de solicitud : {pedidoprov[5]}
                    ''')
        if self.menu.menuSiNo(print1):
            os.system('cls')
            self.base.registrarReposicion(pedidoprov)
            print('\nSolicitud de Productos exitosa.\n')
        else:
            print('\nSe canceló la operación.\n')
    def devolucionProveedor(self,devolucionProv):
            print1 = (f'''\nDevolución a proveedor de...:\n
                    Código de devolución: {devolucionProv[0]}
                    Código de Barra     : {devolucionProv[1]}
                    Cantidad Artículo   : {devolucionProv[2]}
                    CUIL/CUIT Proveedor : {devolucionProv[3]}
                    Fecha de devolución : {devolucionProv[4]}
                    Motivo de devolución: {devolucionProv[5]}
                    ''')
            if self.menu.menuSiNo(print1):
                os.system('cls')
                self.base.devolucionesTabla(devolucionProv)
                self.base.descuentaArticulos(devolucionProv[1],devolucionProv[2])
                print('\nRegistro de devolución exitosa.\n')
            else:
                print('\nSe canceló la operación.\n')