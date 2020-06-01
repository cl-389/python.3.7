# coding: utf-8
# Crear un módulo para validación de nombres de usuarios. Dicho módulo,
# deberá cumplir con los siguientes criterios de aceptación:
"""
- El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12.
- El nombre de usuario debe ser alfanumérico.
- Nombre de usuario con menos de 6 caracteres, retorna el mensaje "El nombre de usuario
  debe contener al menos 6 caracteres".
- Nombre de usuario con más de 12 caracteres, retorna el mensaje "El nombre de usuario
  no puede contener más de 12 caracteres".
- Nombre de usuario con caracteres distintos a los alfanuméricos, retorna el mensaje
  "El nombre de usuario puede contener solo letras y números".
- Nombre de usuario válido, retorna True.
"""


def valid():
    while True:
        non_alfanum = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-',
                       '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\ ', ']', '^',
                       '_', '`', '{', '|', '}', '~', '"']
        a = input("ingrese nombre de usuario: ")
        if len(a) < 6:
            print("El nombre de usuario debe contener al menos 6 caracteres")
        elif len(a) > 12:
            print("El nombre de usuario no puede contener más de 12 caracteres")
        elif set(non_alfanum).intersection(a):
            print("El nombre de usuario puede contener solo letras y números")
        else:
            print("usuario correcto.")
            break


print("el usuario no debe tener mas de 12 caracteres, "
      "ni menos de 6, debe poseer solo letras y numeros.")
print(valid())
