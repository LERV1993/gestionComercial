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
   """
    def altaProv(self,Prov,proveedor):
        IngresoProveedor=self.base.hacerConsulta('Proveedores','CUIL_CUIT_Prov',Prov)
        if not type(IngresoProveedor)==str:
            print1 = (f'''Se va a generar el alta del proveedor:
                    CUIL / CUIT PROV.   : {proveedor[0]}
                    Nombre de Proveedor : {proveedor[1]}
                    Dirección Proveedor : {proveedor[2]}
                    Teléfono Proveedor  : {proveedor[3]}
                    Mail de Proveedor   : {proveedor[4]}
                    Estado IVA Proveedor: {proveedor[5]}
                    ''')
            if menu.menuSiNo(print1):
                os.system('cls')
                self.base.altaProveedor(proveedor)
                print('\nRegistro exitoso.\n')
            else:
                print('\nSe canceló la operación.\n')
        else:
            print("Proveedor ya registrado en Base de Datos...\n")


    def bajaProv(self,Prov,proveedor):
        ingresoProveedor=self.base.hacerConsulta('Proveedores','CUIL_CUIT_Prov',Prov)
        if not type(ingresoProveedor)==str:
            print1 = (f'''\nSe va a generar la baja del proveedor:\n
                    CUIL / CUIT PROV.   : {proveedor[0]}
                    Nombre de Proveedor : {proveedor[1]}
                    Dirección Proveedor : {proveedor[2]}
                    Teléfono Proveedor  : {proveedor[3]}
                    Mail de Proveedor   : {proveedor[4]}
                    Estado IVA Proveedor: {proveedor[5]}
                    ''')
            if menu.menuSiNo(print1):
                os.system('cls')
                self.base.borrarRegistro('Proveedores','CUIL_CUIT_Prov',Prov)
                print('\nSe ha dado de baja a Proveedor.\n')
            else:
                print('\nSe canceló la operación.\n')
        else:
            print("Proveedor no registrado en Base de Datos...")



    def modificarProv(self,Prov,modprov):
        modprov=self.base.hacerConsulta('Proveedores','CUIL_CUIT_Prov',Prov)
        if not type(modprov)==str:
            print1 = (f'''\nSe va a Modificar los datos de proveedor:\n
                    CUIL / CUIT PROV.   : {modificoprov[0]}
                    Nombre de Proveedor : {modificoprov[1]}
                    Dirección Proveedor : {modificoprov[2]}
                    Teléfono Proveedor  : {modificoprov[3]}
                    Mail de Proveedor   : {modificoprov[4]}
                    Estado IVA Proveedor: {modificoprov[5]}
                    ''')
            if menu.menuSiNo(print1):
                os.system('cls')
                self.base.modificarProveedor(Prov,modificoprov)
                print('\nSe ha modificado los datos exitosamente.\n')
            else:
                print('\nSe canceló la operación.\n')
        else:
            print("CUIL/CUIT no registrado en Tabla Proveedores...")


    def pedidoProveedor(self,pedidoprov):
        print1 = (f'''\nSolicitud por OP. de...:\n
                    Número de Orden     : {pedidoprov[0]}
                    Código de Barra     : {pedidoprov[1]}
                    Cantidad Artículo   : {pedidoprov[2]}
                    Nombre de Artículo  : {pedidoprov[3]}
                    Fecha de Solicitud  : {pedidoprov[4]}
                    CUIL/CUIT Proveedor : {pedidoprov[5]}
                    Estado respecto IVA : {pedidoprov[6]}
                    ''')
        if menu.menuSiNo(print1):
            os.system('cls')
            self.base.reposicionTabla(pedidoprov)
            print('\nSolicitud de Productos exitosa.\n')
        else:
            print('\nSe canceló la operación.\n')
    
"""

    def devolucionProveedor(self,Prov):
        devProv=self.base.hacerConsulta('Devoluciones','codigoBarra1',Prov)
        if not type(devProv)==str:
            print1 = (f'''\nDevolución a proveedor de...:\n
                    Código de devolución: {devolucionProv[0]}
                    Código de Barra     : {devolucionProv[1]}
                    Cantidad Artículo   : {devolucionProv[2]}
                    CUIL/CUIT Proveedor : {devolucionProv[3]}
                    Fecha de devolución : {devolucionProv[4]}
                    Motivo de devolución: {devolucionProv[5]}
                    ''')
            if menu.menuSiNo(print1):
                os.system('cls')
                self.base.devolucionesTabla(devolucionProv)
                print('\nRegistro de devolución exitosa.\n')
            else:
                print('\nSe canceló la operación.\n')
        else:
            print("Devolución ya generada...")



GestProv = GestionProveedor()

devolucionProv=[1,125547888888,4,30234568879,"24/05/21",'MEMORIA defectuosa/rota']
#pedidoprov=[1,125547888888,4,'MEMORIA RAM ASTRO 8GB',"24/05/21",30234568879,'inscripto']
#proveedor=[125547888888,4,'MEMORIA RAM ASTRO 8GB',"24/05/21",30234568879,'inscripto']
#modificoprov=[30225474136,'Percant','Brasil 1',1169874521,'juan.perez@percant.com.ar','inscripto']
#GestProv.altaProv(30225474136,proveedor)
#GestProv.BajaProv(30225474136,proveedor)
#GestProv.modificarProv(30225474136,modificoprov)
#GestProv.pedidoProveedor(pedidoprov)
GestProv.devolucionProveedor(125547888888)
