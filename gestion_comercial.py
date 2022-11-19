import os

class gestion_comercial():
    def MenuPrincipal(self):
        print(f'''
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
        self.seleccion = 0
        while True:
            try:
                while self.seleccion<1 or self.seleccion>5:
                    self.seleccion=int(input("        Ingrese Opción Deseada: "))
                    if self.seleccion<1 or self.seleccion>5:
                        print("\nDebe ingresar valor entre 1 y 5...")
                break
            except ValueError:
                print("\nDebe ingresar valor numérico...")    
        if self.seleccion==1:
            os.system("cls")
            self.menu_provedores()
        elif self.seleccion==2:
            os.system("cls")
            self.menu_Clientes()
        elif self.seleccion==3:
            os.system("cls")
            self.menu_Articulos()
        elif self.seleccion==4:
            os.system("cls")
            self.menu_ventas()
        elif self.seleccion==5:
            print("Gracias por utilizar Gestion Interna.")
            print("Saliendo...")
            exit()
        else:
            print("Debe seleccionar una opción del menú...")        

    def menu_provedores(self):
        print(f'''
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
        self.seleccion = 0
        while True:
            try:
                while self.seleccion<1 or self.seleccion>5:
                    self.seleccion=int(input("        Ingrese Opción Deseada: "))
                    if self.seleccion<1 or self.seleccion>5:
                        print("\n Debe ingresar valor entre 1 y 5...")
                break
            except ValueError:
                print("\nDebe ingresar valor numérico...")    
        if self.seleccion==1:
            os.system("cls")
            self.alta_proveedor()
        elif self.seleccion==2:
            os.system("cls")
            self.baja_proveedor()
        elif self.seleccion==3:
            os.system("cls")
            self.modificacion_provedor()
        elif self.seleccion==4:
            os.system("cls")
            self.devolucion()
        elif self.seleccion==5:
            print("Usted esta saliendo de Menu Provedores.")
            print("Saliendo...")
            return self.MenuPrincipal()
        else:
            print("Debe seleccionar una opción del menú...")

    def menu_Clientes(self):
        print(f'''
        -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        --                    "Menu Clientes"                       --
        -----------------------------------------------------------------
        --  1: Alta Clientes --
        --  2: Baja Clientes --
        --  3: Modificacion Clientes --
        --  4: Salir.--
        -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        ''')
        self.seleccion = 0
        while True:
            try:
                while self.seleccion<1 or self.seleccion>5:
                    self.seleccion=int(input("        Ingrese Opción Deseada: "))
                    if self.seleccion<1 or self.seleccion>4:
                        print("\nDebe ingresar valor entre 1 y 4...")
                break
            except ValueError:
                print("\nDebe ingresar valor numérico...")
            
        if self.seleccion==1:
            os.system("cls")
            self.alta_Clientes()
        elif self.seleccion==2:
            os.system("cls")
            self.baja_Clientes()
        elif self.seleccion==3:
            os.system("cls")
            self.modificacion_Clientes()
        elif self.seleccion==4:
            print("Usted esta saliendo de Menu Clientes.")
            print("Saliendo...")
            return self.MenuPrincipal()
        else:
            print("Debe seleccionar una opción del menú...")

    def menu_Articulos(self):
        print(f'''
        -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        --                    "Menu Articulos"                       --
        -----------------------------------------------------------------
        --  1: Alta Articulos --
        --  2: Baja Articulos --
        --  3: Modificacion Articulos --
        --  4: Ingreso de remito.--
        --  5: Listado de articulos --
        --  6: Salir. --
        -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        ''')
        self.seleccion = 0
        while True:
            try:
                while self.seleccion<1 or self.seleccion>6:
                    self.seleccion=int(input("        Ingrese Opción Deseada: "))
                    if self.seleccion<1 or self.seleccion>5:
                        print("\nDebe ingresar valor entre 1 y 6...")
                break
            except ValueError:
                print("\nDebe ingresar valor numérico...")
            
        if self.seleccion==1:
            os.system("cls")
            self.alta_articulos()
        elif self.seleccion==2:
            os.system("cls")
            self.baja_articulos()
        elif self.seleccion==3:
            os.system("cls")
            self.modificacion_articulos()
        elif self.seleccion==4:
            os.system("cls")
            self.ingreso_de_articulo()
        elif self.seleccion ==5:
            os.system("cls")
            self.listado()
        elif self.seleccion==6:
            print("Usted esta saliendo de Menu Articulos.")
            print("Saliendo...")
            return self.MenuPrincipal()    
        else:
            print("Debe seleccionar una opción del menú...")

    def menu_ventas(self):
        print(f'''
        -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        --                    "Menu Ventas "                       --
        -----------------------------------------------------------------
        --  1: Facturacion --
        --  2: Listado de ventas  --
        --  3: Salir --
        -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        ''')
        self.seleccion = 0
        while True:
            try:
                while self.seleccion<1 or self.seleccion>3:
                    self.seleccion=int(input("        Ingrese Opción Deseada: "))
                    if self.seleccion<1 or self.seleccion>5:
                        print("\nDebe ingresar valor entre 1 y 3...")
                break
            except ValueError:
                print("\nDebe ingresar valor numérico...")
            
        if self.seleccion==1:
            os.system("cls")
            self.facturacion()
        elif self.seleccion==2:
            os.system("cls")
            self.listado_ventas()
        elif self.seleccion==3:
            print("Usted esta saliendo de Menu Ventas.")
            print("Saliendo...")
            return self.MenuPrincipal()    
        else:
            print("Debe seleccionar una opción del menú...")
            

pepito = gestion_comercial()
pepito.MenuPrincipal()


         