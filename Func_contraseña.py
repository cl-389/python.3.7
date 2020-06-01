# coding: utf-8
# Crear un módulo para validación de contraseñas.
# Dicho módulo, deberá cumplir con los siguientes criterios de aceptación:
"""
- La contraseña debe contener un mínimo de 8 caracteres. --> cadena<8=false
- Una contraseña debe contener letras minúsculas, mayúsculas,
  números y al menos 1 carácter no alfanumérico. --> islower(), isupper().
- La contraseña no puede contener espacios en blanco. --> for i in cadena _--> if(i==" ") _-->cadena = true
- Contraseña válida, retorna True.
- Contraseña no válida, retorna el mensaje "La contraseña
  elegida no es segura".
pendiente de re vision en Fuuncion y bucle while
"""


def contras():
    a = False
    while not a:

        import curses.ascii
        vld1 = 0
        vld2 = 0
        vld3 = 0
        vld4 = 0
        A = input("ingrese Contraseña: ")
        for i in A:
            if i == " ":
                vld1 = 1 * 1
            elif i != " ":
                vld1 = vld1 + 0
        for i in A:
            if curses.ascii.islower(i):
                vld2 = 1 * 1
            elif not curses.ascii.islower(i):
                vld2 = vld2 + 0
        for i in A:
            if curses.ascii.isupper(i):
                vld3 = 1 * 1
            elif not curses.ascii.isupper(i):
                vld3 = vld3 + 0
        for i in range(len(A)):
            if i < 7:
                vld4 = 0
            elif i >= 7:
                vld4 = 1 * 1
        if (vld1 == 0) and (vld2 == 1) and (vld3 == 1) and (vld4 >= 1):
            print("Contraseña aceptada")
            a = True
        else:
            a = False
    return a


print("crear contraseña: con mas de 8 caracteres, "
      "que incuyan mayusculas y minusculas, y que no posea espacios.")
print(contras())
input("presiona cualquier tecla para salir") 
