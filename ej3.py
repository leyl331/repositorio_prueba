# imprimir mensaje personalizado

def mensaje():
    nombre = input("Ingrese su nombre : ")
    edad = input("Ingrese su edad : ")
    profesion = input("Ingrese su profesion :  ")
    
    mensaje = (f"Hola, {nombre}, usted tiene {edad} años y trabaja como {profesion}. "
               "¡Gracias por llenar ingresar sus datos!")
    print(mensaje)

mensaje()

