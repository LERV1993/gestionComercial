from gestionArticulos import *
from gestionCliente import *
from gestionProveedor import *
from OpcMenu import *

class GestionComercial (object):
    menuGral = print(f'''
        -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        --                    "Gestion interna"                    --
        -----------------------------------------------------------------
        --  1: Menu Proveedores --
        --  2: Menu Clientes --
        --  3: Menu Articulos --
        --  4: Menu Ventas --
        --  5: Salir.--
        -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        ''')
    