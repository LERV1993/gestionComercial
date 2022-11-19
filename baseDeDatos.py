import mariadb

class BaseDeDatos(object):
    def __init__(self):
        self.bd = mariadb.connect(
        host="localhost",
        port=4005,
        user="root",
        password="",
        autocommit=True
        )
        self.cursor = self.bd.cursor()
    def crearBase(self):
        try:
            self.cursor.execute("CREATE DATABASE Gestion_Comercial")
        except mariadb.Error:
            return(f"\nLa base de datos Gestión Comercial, ya habia sido creada.")
    def conectarBaseDeDatos(self):
        self.bd =mariadb.connect(
        host="localhost",
        port=4005,
        user="root",
        password="",
        db = "Gestion_Comercial"
        )
        self.cursor = self.bd.cursor()
    def clientesTabla(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Clientes(DNI_Cli INT PRIMARY KEY,NombreCli VARCHAR (255),ApellidoCli VARCHAR(255),direccionCli VARCHAR(255),telefonoCli BIGINT,mailCli VARCHAR(255),estadoIvaCli VARCHAR(255))")
    def proveedoresTabla(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Proveedores(CUIL_CUIT_Prov BIGINT PRIMARY KEY,Nombre_Prov VARCHAR(255),Direccion_Prov VARCHAR(255),Telefono_Prov BIGINT,Mail_Prov VARCHAR(255),estadoIvaProv VARCHAR(255))")
    def articulosTabla(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Articulos(codigoBarra BIGINT PRIMARY KEY,nombreArticulo VARCHAR(255),categoriaArt VARCHAR(255),precioArt DECIMAL(8,2),cantidadArt INT,CUIL_CUIT_Prov BIGINT)")
    def devolucionesTabla(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Devoluciones(codigoDevolucion INT PRIMARY KEY, codigoBarra BIGINT,cantidadArt INT,motivoDev VARCHAR(255),fecha DATE)")
    def ventasTabla(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Ventas(CodigoVent INT AUTO_INCREMENT PRIMARY KEY,fechaVenta DATE,Factura BIGINT,codigoBarraVent BIGINT,nombreArticuloVent VARCHAR(255),CantidadVent INT,DNI_Cli_Vent INT,NombreCli VARCHAR(255),ApellidoCli VARCHAR(255),estadoIvaCli VARCHAR(255))")                                                                                                          
    def agregarValores(self):
        sql = "INSERT INTO Clientes (DNI_Cli, NombreCli, ApellidoCli, direccionCli, telefonoCli, mailCli, estadoIvaCli) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = [
            (40123033,'Antonella', 'Lopez','Superi 1111',1512345678,'antonella.lopez@hotmail.com','Inscripto'),
            (38526847,'Camila', 'Gomez','Monreo 2587',1599887766,'camila.gomez@hotmail.com','Exento'),
            (35554845,'Laura', 'Diaz','Cabildo 3333',1522334455,'laura.diaz@hotmail.com','Inscripto'),
            (36345584,'Luis', 'Ruiz','Juramento 1300',1154585978,'luis.ruiz@hotmail.com','Final'),
            ]
        self.cursor.executemany(sql,val)
        self.bd.commit()
        sql = "INSERT INTO Proveedores (CUIL_CUIT_Prov, Nombre_Prov, Direccion_Prov, Telefono_Prov, Mail_Prov, estadoIvaProv) VALUES (%s, %s, %s, %s, %s,%s)"
        val = [
            (30234568879,'Astro','Montana 125',1168674500,'carla.suarez@astro.com','Inscripto'),
            (20369552458,'SMG e hijos','Peron 4500',1123258744,'diego.gregorio@smg.com.ar','Inscripto'),
            (20159753354,'Fabian Quinteros','Piedras 25',1145587454,'fabian_1987@hotmail.com','Inscripto'),
            (30225474136,'Percant','Brasil 600',1169874521,'juan.perez@percant.com.ar','Inscripto')
        ]
        self.cursor.executemany(sql,val)
        self.bd.commit()
        sql = "INSERT INTO Articulos (codigoBarra, nombreArticulo, categoriaArt, precioArt, cantidadArt, CUIL_CUIT_Prov) VALUES (%s, %s, %s, %s, %s,%s)"
        val = [
            (2035000025547888888,'MEMORIA RAM ASTRO 8GB','Memorias',2300.50,4,30234568879),
            (2035000025547855555,'CPU CORE I3 INTEL','Procesadores',33000.98,3,20159753354),
            (2035000025547866666,'GABINETE SMG 2300','Gabinetes',12000.00,3,20369552458),
            (2035000025547877777,'FUENTE 650W PERCANT 80GOLD PLUS','Fuentes',6000.00,3,30225474136)
        ]
        self.cursor.executemany(sql,val)
        self.bd.commit()
    def agregarCliente(self,nuevoCliente):
        sql = "INSERT INTO Clientes (DNI_Cli, NombreCli, ApellidoCli, direccionCli, telefonoCli, mailCli, estadoIvaCli) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql,nuevoCliente)
        self.bd.commit()
    def agregarProveedor(self,nuevoProveedor):
        sql = "INSERT INTO Proveedores (CUIL_CUIT_Prov, Nombre_Prov, Direccion_Prov, Telefono_Prov, Mail_Prov, estadoIvaProv) VALUES (%s, %s, %s, %s, %s,%s)"
        self.cursor.execute(sql,nuevoProveedor)
        self.bd.commit()
    def agregarArticulo(self,nuevoArticulo):
        sql = "INSERT INTO Articulos (codigoBarra, nombreArticulo, categoriaArt, precioArt, cantidadArt, CUIL_CUIT_Prov) VALUES (%s, %s, %s, %s, %s,%s)"
        self.cursor.execute(sql,nuevoArticulo)
        self.bd.commit()
    def registrarVenta(self,nuevaVenta):
        sql = "INSERT INTO Ventas (fechaVenta,Factura,codigoBarraVent,nombreArticuloVent,CantidadVent,DNI_Cli_Vent,NombreCli,ApellidoCli,estadoIvaCli) VALUES (%s, %s, %s, %s,%s, %s, %s,%s,%s)"
        self.cursor.execute(sql,nuevaVenta)
        self.bd.commit()
    def registraDevolución(self,nuevaDevolucion):
        sql = "INSERT INTO Devoluciones (codigoDevolucion, codigoBarra,cantidadArt,motivoDev,fecha) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(sql,nuevaDevolucion)
        self.bd.commit()
    def descuentaArticulos(self,codigoArt,cantADescontar):
        self.cursor.execute(f"SELECT * FROM Articulos where codigoBarra = {codigoArt}")
        resultado = self.cursor.fetchone()
        registro = []
        for campo in resultado:
            registro.append(campo)
        cantidad = registro[4] - cantADescontar
        self.cursor.execute(f"UPDATE Articulos SET cantidadArt = '{cantidad}' WHERE codigoBarra = {codigoArt}")
        self.bd.commit()
   
   
    def verTablaClientes(self):
        self.cursor.execute("SELECT DNI FROM Clientes")
        dni_clientes=[]
        for ind in self.cursor:
            dni_clientes.append(ind)
        if len(dni_clientes) > 0:
            return True
        else:
            return False
    def verTablaLibros(self):
        self.cursor.execute("SELECT ISBN FROM Libros")
        isbn_libros=[]
        for ind in self.cursor:
            isbn_libros.append(ind)
        if len(isbn_libros)> 0:
            return True
        else:
            return False
    def hacerConsulta(self,tabla,campo,dato):
        self.cursor.execute(f"SELECT * FROM {tabla} where {campo} = {dato}")
        resultado = self.cursor.fetchone()
        if not (resultado) is None:
            listaResultado = []
            for registro in resultado:
                listaResultado.append(registro)
            return listaResultado
        else:
            return("\nNo hay registros para el dato consultado.")
    def cantidadDeRegistros(self,tabla):
        self.cursor.execute(f"SELECT * FROM {tabla} LIMIT 100")
        registros = self.cursor.fetchall()
        return(registros)
    def actualizarRegistros(self,tabla,campo,datomodificado,campoID,regId):
        self.cursor.execute(f"UPDATE {tabla} SET {campo} = '{datomodificado}' WHERE {campoID} = {regId}")
        self.bd.commit()
    def borrarRegistro(self,tabla,campo,condicion):
        sql = f"DELETE FROM {tabla} WHERE {campo} LIKE '%{condicion}%'"
        self.cursor.execute(sql)
        self.bd.commit()

venta = ['2022-11-04',100235652554789522,2035000025547888888,'MEMORIA RAM ASTRO 8GB',1,40123033,'Antonella','Lopez','Inscripto']
base = BaseDeDatos()
base.crearBase()
base.conectarBaseDeDatos()
base.clientesTabla()
base.proveedoresTabla()
base.articulosTabla()
base.devolucionesTabla()
base.ventasTabla()
base.registrarVenta(venta)
#base.agregarValores()
#base.agregarCliente()

## -------------------  Ejemplos de formato de datos -----------------------------
#cliente = [40123033,'Antonella', 'Lopez','Superi 1111',1512345678,'antonella.lopez@hotmail.com','Inscripto']

#articulo = [2035000025547888888,'MEMORIA RAM ASTRO 8GB','Memorias',2300.50,4,30234568879]

#proveedor = [30234568879,'Astro','Montana 125',1168674500,'carla.suarez@astro.com','Inscripto']

##### VENTA no se registra el codigo de venta ya que este posee un id auto incremental
#venta = ['2022-11-04',100235652554789522,2035000025547888888,'MEMORIA RAM ASTRO 8GB',1,40123033,'Antonella','Lopez','Inscripto']

#devolucion = ['11235552',2035000025547888888,1,'Falla en Gtia','2022-11-04']

#formato de Fecha '2022-11-04'

# Las funciones que registran nuevos campos estan seteadas para que los argumentos sean listas