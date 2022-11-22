import os

class Validacion(object):
    def numero(self,loQueSea,mayorQue,menorQue):
        ingreso = 0
        while True:
            try:
                while ingreso < mayorQue or ingreso > menorQue:
                    ingreso = int(input(f"\nIngrese el {loQueSea}: "))
                    if ingreso < mayorQue or ingreso > menorQue:
                        os.system('cls')
                        print(f"\nEl {loQueSea} debe tener un valor entre {mayorQue} y {menorQue}.")
                break
            except ValueError:
                os.system('cls')
                print("\nPro favor ingrese valores numéricos")
        return ingreso      
    def stringSinNum(self,loQueSea):
        ingreso =""
        validar = True
        while True:
            try:
                while validar == True or len(ingreso) < 1 or len(ingreso) >30:
                    ingreso = input(f"\nIngrese el {loQueSea}: ").title()
                    if len(ingreso) < 1 or len(ingreso) >30:
                        os.system('cls')
                        print(f"\nEl {loQueSea} debe tener entre 1 y 30 caracteres.")
                    cont = 0
                    for elemento in ingreso:
                        if not elemento.isdigit():
                            cont += 1
                    if cont != len(ingreso):
                        os.system('cls')
                        print(f"\nPor favor ingrese sólo letras para el {loQueSea}.")
                    else:
                        validar = False
                break
            except ValueError:
                os.system('cls')
                print("\nOcurrió un error.")
        return ingreso
    def string30(self,loQueSea):
        ingreso =""
        while True:
            try:
                while len(ingreso) < 1 or len(ingreso) >30:
                    ingreso = input(f"\nIngrese {loQueSea}: ")
                    if len(ingreso) < 1 or len(ingreso) >30:
                        os.system('cls')
                        print(f"\n{loQueSea} debe tener entre 1 y 30 caracteres.")
                break
            except ValueError:
                os.system('cls')
                print("\nOcurrió un error.")
        return ingreso