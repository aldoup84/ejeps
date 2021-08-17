import math
import os
def main():
    os.system("clear")
    radio = float(input("Escribe el valor del radio de la esfera: "))
    vol = 4 / 3 * math.pi * math.pow(radio,3)
    print(f"El volumen de la esfera de {radio} radio es de {vol} cm3") 

if __name__=='__main__':
    main()
