import os 

class OpcMenu(object):
    def __init__(self,menu):
        self.seleccion = 0
        self.menustr = menu
    def selMenu(self):
        os.system('cls') 
        print(self.menustr) 
        self.seleccion=0                                                        
        while True:                                                        
            try:
                while self.seleccion<1 or self.seleccion>4:                          
                    self.seleccion=int(input(f'\nIngrese en N° de la opcion deseada a realizar:  '))  
                    if self.seleccion<1 or self.seleccion>4:
                        os.system('cls')                                               
                        print('\nPor favor ingrese un valor entre 1 y 4: \n' , self.menustr)
                break
            except ValueError:
                os.system('cls')                                                                                                                                         
                print('\nPor favor ingrese un valor numerico.\n',self.menustr)
        return self.seleccion