# Ejercicio 01
texto01="aquellos que contemplan la belleza de la tierra, encuentran fuerzas que duraran para siempre"
print("Texto01: ", texto01)
# Convertir el texto01 de minusculas a mayusculas
texto01_mayuscula=texto01.upper()
print(texto01_mayuscula)


# Ejercicio 02
texto02="LA NATURALEZA NO ES UN LUJO, SINO UNA NECESIDAD DEL ESPIRITU HUMANO"
print("Texto02: ", texto02)
# Convertir el texto02 a minusculas
texto02_minuscula=texto02.lower()
print(texto02_minuscula)


# Ejercicio 03
texto03="a todo el mundo le gusta hablar de la sociedad, pero no habra sociedad si no cuidamos el medio ambiente"
print("Texto03: ", texto03)
# Mostrar el numero de ocurrencias de la palabara sociedad
print("sociedad -> ",texto03.count("sociedad"))                 # Devuelve 2
# Mostrar el numero de ocurrencias de la vocal e
print("e -> ",texto03.count("e"))                               # Devuelve 10


# Ejercicio 04
texto04="te dejaste por cobarde, yo te olvide por valiente"
print("Texto04: ",texto04)
# Reemplazar "te" por "me"
print(texto04.replace("te","me"))
# Reemplazar  "dejaste" por "olvidaste"
print(texto04.replace("dejaste","olvidaste de mi"))


# Ejercicio 05
texto05="     no te deseo nada malo, no te tengo odio; eso seria un esfuerzo demasiado grande, no eres tan importante        "
print("Texto05: ", texto05)
# Limpiar los espacios en blanco en la izquierda
print(texto05.lstrip())
# Limpiar los espacios en blanco a la derecha
print(texto05.rstrip())


# Ejercicio 06
texto06="no tengas miedo a perder a alguien que no se siente afortunado de tenerte"
print("Texto06: ", texto06)
# Comprobar si el texto06 , esta compuesto de numeros
print(texto06.isdigit())      # Devuelve False


# Ejercicio 07
texto07="el exito es un mal profesor, seduce a las personas inteligentes a pensar que no pueden fallar nunca"
print("Texto07: ", texto07)
# Comprobar si el texto07 es alfanumerico
print(texto07.isalnum())         # Devuelve False


# Ejercicio 08
texto08="hay solo dos grandes tragedias en la vida: una es no conseguir lo que quieres y la otra es conseguirlo"
print("Texto08: ", texto08)
# Comprobar si el texto08, tiene caracteres de alfabeto
print(texto08.isalpha())   # Devuelve False


# Ejercicio 09
texto09="aprende de ayer, vive para hoy, ten esperanza para manana; lo importante es no dejar de preguntar"
print("Texto09: ", texto09)
# Comprobar si el texto09 es imprimible
print(texto09.isprintable())          # Devuelve True


# Ejercicio 10
texto10="#un#matrimonio#exitoso#requiere#enamorarse#muchas#veces,#siempre#con#la#misma#persona"
print("Texto10: ", texto10)
# Dividir la cadena (#)
texto10_dividir=texto10.split("#")
print(texto10_dividir)
# Otra forma de vividir
for item in texto10_dividir:
    print(item)


# Ejercicio 11
texto11="cuando te miro, mi mente se queda en blanco y mi corazon late mas rapido"
print("Text11: ", texto11)
# Reemplazar blanco por negro,late por palpita y convertir a mayuscula el texto11
print(texto11.replace("blanco","negro").replace("late","palpita").upper())


# Ejercicio 12
texto12="           ERES UN SER ADORABLE, ESTUDIO TUS PIES CON EL MICROSCOPIO Y TU ALMA CON EL TELESCOPIO"
print("Texto12: ", texto12)
# Limpiar espacios en la izquierda y convrtir a minusculas
print(texto12.lstrip().lower())


# Ejercicio 13
texto13="creo%que%ya%me%puedo%morir%feliz,%porque%acabo%de%ver%un%pedazo%de%cielo"
print("Texto13: ", texto13)
# Dividir el texto13
texto13_dividir=texto13.split("%")
for item in texto13_dividir:
    print(item)


# Ejercicio 14
texto14="el que tiene grandes pensamientos, a menudo comete grandes errores"
print("Texto14: ", texto14)
# Mostrar el numero de ocurrencia de las vocales a, e , i, o, u en el texto14
print("a: ",texto14.count("a"))        # Devuelve 4
print("e: ",texto14.count("e"))        # Devuelve 13
print("i: ",texto14.count("i"))        # Devuelve 2
print("o: ",texto14.count("o"))        # Devuelve 4
print("u: ",texto14.count("u"))        # Devuelve 2


# Ejercicio 15
texto15="#la naturaleza es la mejor maestra de la verdad"
print("Texto15: ", texto15)
# Reemplazar naturaleza por vegetacion, verdad por realidad y retornar el texto15 a mayusculas
print(texto15.replace("naturaleza","vegetacion").replace("verdad","realidad").upper())
# Retornar el texto en formato Camel Case
print(texto15.title())
# Comprobar si el texto empieza con #
print(texto15.startswith("#"))         # Devuelve True
