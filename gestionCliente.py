from baseDeDatos import BaseDeDatos
from OpcMenu import *
import os

class Gestion_Cliente(object):
    def __init__(self):
        self.base = BaseDeDatos()
        self.base.inicializacionBase()
        self.menu = opcMenu()
              
    def altaCliente(self,dni_cliente,cliente):
        clienteporagregar = self.base.hacerConsulta("Clientes","DNI_Cli",dni_cliente)  
        if type(clienteporagregar) == str:
            print1=(f'''Se generara el alta del cliente: 
                  DNI de cliente: {cliente[0]}
                  Nombre de cliente: {cliente[1]}
                  Apellido cliente: {cliente[2]}
                  Direccion: {cliente[3]}
                  Telefono: {cliente[4]}
                  Email: {cliente[5]}
                  Situacion IVA: {cliente[6]}
                ''')   
            if self.menu.menuSiNo(print1):
                os.system("cls")
                self.base.altaCliente(cliente)
                print("\n Registro exitoso.")
            else:
                print("\nSe canceló la operación.")     
        else:
            print("\nEl cliente que se quiere dar de alta ya está registrado")          
    
    def borrarCliente(self,dni_cliente,cliente):
        r = self.base.hacerConsulta("Clientes","DNI_Cli",dni_cliente)  
        if not type(r) == str:
            print1=(f'''Clientes a borrar: 
                DNI de cliente: {cliente[0]}
                Nombre de cliente: {cliente[1]}
                Apellido cliente: {cliente[2]}
                Direccion: {cliente[3]}
                Telefono: {cliente[4]}
                Email: {cliente[5]}
                Situacion IVA: {cliente[6]}
                ''')
            if self.menu.menuSiNo(print1):
                os.system("cls")
                self.base.borrarRegistro("Clientes","DNI_Cli",dni_cliente)
                print("\n Cliente eliminado exitosamente.")
            else:
                print("\nSe canceló la operación.")     
        else:
            print("\nEl DNI no se encuentra registrado.")
            
    def modi_Clientes(self,dni_cliente,cliente):
        r = self.base.hacerConsulta("Clientes","DNI_Cli",dni_cliente)  
        if not type(r) == str:
            print1=(f'''Clientes a modificar: 
                DNI de cliente: {cliente[0]}
                Nombre de cliente: {cliente[1]}
                Apellido cliente: {cliente[2]}
                Direccion: {cliente[3]}
                Telefono: {cliente[4]}
                Email: {cliente[5]}
                Situacion IVA: {cliente[6]}
                ''')
            if self.menu.menuSiNo(print1):
                os.system("cls")
                self.base.modificarCliente(dni_cliente,x)
                print("\nModificación de cliente exitosa.")
            else:
                print("\nSe canceló la operación.")
        else:
            print("\nEl DNI no corresponde a un cliente registrado.")
        
                
pepito = Gestion_Cliente()
x = [40123033,'Antonella', 'Lopez','Superi 1111',1512345678,'antonella.lopez@hotmail.com','Inscripto']
f = [38526847,'Camila', 'Gomez','Monreo 2587',1599887766,'camila.gomez@hotmail.com','Exento']
#pepito.altaCliente(38526847,f)          
#pepito.borrarcliente(38526847,f)
pepito.modi_Clientes(38789664,x)