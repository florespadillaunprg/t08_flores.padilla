#Ejercicio 1
text1="     donde hay amor no hay pecado        "
print("Texto 01: ", text1)
# Limpiar los espacios en blanco en la izquierda
print(text1.lstrip())
# Limpiar los espacios en blanco a la derecha
print(text1.rstrip())




#Ejercicio 2
text2="ojos que no ven corazon que no siente"
print("Texto 02: ", text2)
# Comprobar si el texto 02 es imprimible
print(text2.isprintable())          # Muestra True




#Ejercicio 3
text3="#desgraciado en el juego, afortunado en el amor"
print("Texto 03: ", text3)
# Reemplazar juego por terreno, amor por dinero y retornar el texto 03 a mayusculas
print(text3.replace("juego","terreno").replace("amor","dinero").upper())
# Retornar el texto en formato Camel Case
print(text3.title())
# Comprobar si el texto empieza con #
print(text3.startswith("#"))         # Devuelve True




#Ejercicio 4
text4="no hay rosas sin espinas"
print("Texto 04: ", text4)
# Convertir el texto 04 de minusculas a mayusculas
text4_mayuscula=text4.upper()
print(text4_mayuscula)




#Ejercicio 5
text5="para torear y amarse, hay que arrimarse"
print("Texto 05: ", text5)
# Reemplazar torear por engañar, amarse por enamorarse y convertir a mayuscula el texto 05
print(text5.replace("torear","engañar").replace("amarse","enamorarse").upper())





#Ejercicio 6
text6="#que#bien#te#quiere,#te#hara#llorar"
print("Texto 06: ", text6)
# Dividir la cadena (#)
text6_dividir=text6.split("#")
print(text6_dividir)
# Otra forma de vividir
for item in text6_dividir:
    print(item)



#Ejercicio 7
text7="A AMOR Y FORTUNA, RESISTENCIA NINGUNA"
print("Texto 07: ", text7)
# Convertir el texto 07 a minusculas
text7_minuscula=text7.lower()
print(text7_minuscula)




#Ejercicio 8
text8="el amor es ciego pero el matrimonio lo cura"
print("Texto 08: ", text8)
# Comprobar si el texto 08 es alfanumerico
print(text8.isalnum())         # Devuelve False



#Ejercicio 9
text9="ama$al$grado$que$quieras$ser$amado$"
print("Texto 09: ", text9)
# Dividir el texto 9
text9_dividir=text9.split("$")
for item in text9_dividir:
    print(item)





#Ejercicio 10
text10="amor loco si tu quieres mucho y ella te quiere poco"
print("Texto 10: ",text10)
# Reemplazar "si" por "es que"
print(text10.replace("si","es que"))
# Reemplazar  "ella" por "el"
print(text10.replace("ella","el"))




#Ejercicio 11
text11="el que ama a una casada, puede morir de cornada"
print("Texto 11: ", text11)
# Mostrar el numero de ocurrencias de la palabara sociedad
print("casada -> ",text11.count("casada"))                 # Devuelve 1
# Mostrar el numero de ocurrencias de la vocal e
print("a -> ",text11.count("a"))                          # Devuelve 9




#Ejercicio 13
text13="me gustas cuando callas porque estas como ausente"
print("Texto 13: ", text13)
# Comprobar si el texto 13 , esta compuesto de numeros
print(text13.isdigit())      # Devuelve False



#Ejercicio 14
text14="           TODO ESTA PERMITIDO EN EL AMOR"
print("Texto 14: ", text14)
# Limpiar espacios en la izquierda y convrtir a minusculas
print(text14 .lstrip().lower())





#Ejercicio 15
texto15="puedo escribir los versos más tristes esta noche"
print("Texto 15: ", texto15)
# Mostrar el numero de ocurrencia de las vocales a, e , i, o, u en el texto 15
print("a: ",texto15.count("a"))        # Devuelve 1
print("e: ",texto15.count("e"))        # Devuelve 6
print("i: ",texto15.count("i"))        # Devuelve 3
print("o: ",texto15.count("o"))        # Devuelve 4
print("u: ",texto15.count("u"))        # Devuelve 1
