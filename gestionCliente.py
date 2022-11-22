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
    
    def borrarCliente(self,dni_cliente):
        clienteABorrar = self.base.hacerConsulta("Clientes","DNI_Cli",dni_cliente)  
        if not type(r) == str:
            print1=(f'''Clientes a borrar: 
                DNI de cliente: {clienteABorrar[0]}
                Nombre de cliente: {clienteABorrar[1]}
                Apellido cliente: {clienteABorrar[2]}
                Direccion: {clienteABorrar[3]}
                Telefono: {clienteABorrar[4]}
                Email: {clienteABorrar[5]}
                Situacion IVA: {clienteABorrar[6]}
                ''')
            if self.menu.menuSiNo(print1):
                os.system("cls")
                self.base.borrarRegistro("Clientes","DNI_Cli",dni_cliente)
                print("\n Cliente eliminado exitosamente.")
            else:
                print("\nSe canceló la operación.")     
        else:
            print("\nEl DNI no se encuentra registrado.")
            
    def modiClientes(self,dni_cliente):
        clienteAModificar = self.base.hacerConsulta("Clientes","DNI_Cli",dni_cliente)  
        if not type(r) == str:
            print1=(f'''Clientes a modificar: 
                DNI de cliente: {clienteAModificar[0]}
                Nombre de cliente: {clienteAModificar[1]}
                Apellido cliente: {clienteAModificar[2]}
                Direccion: {clienteAModificar[3]}
                Telefono: {clienteAModificar[4]}
                Email: {clienteAModificar[5]}
                Situacion IVA: {clienteAModificar[6]}
                ''')
            if self.menu.menuSiNo(print1):
                os.system("cls")
                self.base.modificarCliente(dni_cliente,clienteAModificar)
                print("\nModificación de cliente exitosa.")
            else:
                print("\nSe canceló la operación.")
        else:
            print("\nEl DNI no corresponde a un cliente registrado.")
