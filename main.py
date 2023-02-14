

print("Nombre: Mayda Daniela Matul Alvarado, Carné: 1535523")

import os 

mi ubicacion = os.getcwd()
if os.path.exists("modulos"):
    print("La carpeta ya existe")
else: 
    os.mkdir(mi ubicacion + "\\modulos")
    archivo = open('/modulos/prueba.txt', 'w')
    archivo.write('Hola mundo')
    archivo-close()