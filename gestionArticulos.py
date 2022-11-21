from baseDeDatos import BaseDeDatos

class GestionArticulos(object):
    def __init__(self):
        base = BaseDeDatos()
        base.crearBase()
        base.conectarBaseDeDatos()
        base.clientesTabla()
        base.proveedoresTabla()
        base.articulosTabla()
        base.ventasTabla()
        base.devolucionesTabla()
        base.reposicionTabla()

