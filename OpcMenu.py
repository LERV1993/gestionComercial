import os 

class opcMenu (object):
    def menuNum(self,menuPrint,cantidadDeOpciones):
        os.system('cls') 
        seleccion = 0
        while True:                                                        
            try:
                while seleccion < 1 or seleccion > cantidadDeOpciones: 
                    print(menuPrint)                         
                    seleccion=int(input(f'\nIngrese en N° de la opcion deseada a realizar:  ')) 
                    if seleccion < 1 or seleccion > cantidadDeOpciones:
                        os.system('cls')                                               
                        print(f'\nPor favor ingrese un valor entre 1 y {cantidadDeOpciones}: ')
                break
            except ValueError:
                os.system('cls')                                                                                                                                         
                print('\nPor favor ingrese un valor numerico.')
        return seleccion
    def menuSiNo(self,menuPrint):
        os.system('cls') 
        seleccion = ""
        while True:
            try:
                while seleccion!="si" and seleccion!="no":
                    print(menuPrint)
                    seleccion = input("\nConfirma ? Si/No: ").lower()
                    if seleccion!="si" and seleccion!="no":
                        os.system('cls')
                        print('Por favor ingrese "Si" o "No".')
                break
            except ValueError:
                os.system('cls') 
                print('\nPor favor ingrese si o no, otro ingreso es invalido.')
        if seleccion == 'si':
            return True
        else:
            return False