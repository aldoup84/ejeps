import math
import os
def main():
    os.system("clear")
    lado = float(input("Escribe el valor del lado de un cuadrado: "))
    perimetro = 4 * lado
    area = math.pow(lado,2)
    print ("El perimetro es: " + str(lado) + " es: " + str(perimetro))
    print (f"El area del cuadrado de lado {lado} es: {area}") 


if __name__=='__main__':
    main()
