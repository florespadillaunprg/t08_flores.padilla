# Ejercicio 01
#                  10        20        30        40        50        60        70
#         0123456789012345678901234567890123456789012345678901234567890123456789012345
refran01="Reflexionando y dialogando, el hombre es capaz de desenredar todos los nudos"
print("Refran01: ", refran01)
print(refran01.find("todos"))         # Devuelve 61
print(refran01.index("a"))            # Devuelve 9


# Ejercicio 02
#                  10        20        30        40        50        60        70        80        90
#         012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678
refran02="Hay quienes piensan que el dinero lo es todo, por eso se rebajan a cualquier cosa por hacerse ricos"
print("Refran02: ",refran02)
# Devolver codigo 1234
print(refran02.find("a"),refran02.find("y"),refran02.find(" "),refran02.find("q"))


# Ejercicio 03
#                  10        20        30        40        50        60        70
#         0123456789012345678901234567890123456789012345678901234567890123456789012345678
refran03="Si quieres ser feliz, no solo tendras que pasar pagina, sino cerrar bibliotecas"
print("Refran03: ", refran03)
# Devolver mi numero de celular 97 43 56 0 76
print(refran03.index("s"),refran03.index("r"),refran03.index("asa"),refran03.index("si"),refran03.index("S"),refran03.index("cas"))


# Ejercicio 04
#                  10        20        30        40        50        60        70        80        90       100
#         01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123
refran04="La disculpa no siempre es el reflejo de la razon, sino el de nuestro amor por alguien por encima del ego"
print("Refran04: ", refran04)
# Devolver 56 100 0 verticalmente
print(refran04.index("l d"))   # Devuelve 56
print(refran04.find(" ego"))   # Devuelve 100
print(refran04.find("L"))      # Devuelve 0


# Ejercicio 05
#                  10        20        30        40        50        60        70
#         012345678901234567890123456789012345678901234567890123456789012345678901
refran05="La cultura de una nacion reside en los corazones y las almas de su gente"
print("Refran05: ", refran05)
print(refran05.index("de en"))     # Devuelve 29
print(refran05.find("mas"))        # Devuelve 57


# Ejercicio 06
#                  10        20        30        40        50        60        70        80        90
#         01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567
refran06="Cuando debes tomar una decision, mira hacia tu corazon y hacia tu alma primero, no hacia tu cabeza"
print("Refran06: ", refran06)
print(refran06.find("ro,"))           # Devuelve 76
print(refran06.index("acia"))         # Devuelve 39

# Ejercicio 07
#                  10        20        30        40        50        60        70        80        90       100
#         01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123
refran07="El secreto esta en confiar siempre en tu alma y en tu corazon, pues solo asi podras escaparte del horror"
print("Refran07: ", refran07)
print(refran07.index("rror"))         # Devuelve 100
print(refran07.find("fiar"))          # Devuelve 22


# Ejercicio 08
#                  10        20        30        40        50        60        70
#         01234567890123456789012345678901234567890123456789012345678901234567890123456
refran08="La pobreza de bienes es facilmente remediable, mas la del alma es irreparable"
print("Refran08: ", refran08)
print(refran08.index("facil"))        # Devuelve 24
print(refran08.find(", mas"))         # Devuelve 45


# Ejercicio 09
#                  10        20        30        40        50        60        70        80        90
#         01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567
refran09="No te sientas mal por ser cada vez mas viejo, pues no hay nada mejor que un alma con mas sabiduria"
print("Refran09: ", refran09)
print(refran09.index("cada"),":" ,refran09.find("or"))       # Devuelve 26 :19


# Ejercicio 10
#                  10        20        30        40        50        60        70
#         012345678901234567890123456789012345678901234567890123456789012345678901234567
refran10="Si la tristeza marchita tu corazon, deja que tu alma reivindique esa sensacion"
print("Refran10: ", refran10)
print(refran10.index("mar"),",",refran10.find("indique"),"y",refran10.index("triste"))      # Devuelve 15 , 57 y 6


# Ejercicio 11
#                  10        20        30        40        50        60        70
#         01234567890123456789012345678901234567890123456789012345678901234567890123
refran11="La educacion se mide por lo mucho que logras enriquecer el alma de un nino"
print("Refran11: ", refran11)
print(refran11.index("p"))          # Devuelve 21
print(refran11.index("alma"))       # Devuelve 59


# Ejercicio 12
#                  10        20        30        40        50        60        70        80        90
#         0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456
refran12="No tomes una decision basandote unicamente en la razon, pues solo estarias menospreciando tu alma"
print("Refran12: ", refran12)
print(refran12.find(" p"))                                                          # Devuelve 55
print(refran12.index("rias"),"-",refran12.find("n b"),"=",refran12.find("az"))      # Devuelve 70 - 20 =50


# Ejercicio 13
#                  10        20        30        40        50        60        70
#         0123456789012345678901234567890123456789012345678901234567890123456789012345
refran13="Vive tu vida como si cada día fuese el ultimo; solo asi estara llena el alma"
print("Refran13: ", refran13)
print(refran13.find(""))       # Devuelve 0
print(refran13.index(";"))     # Devuelve 45


# Ejercicio 14
#                  10        20        30        40        50        60
#         0123456789012345678901234567890123456789012345678901234567890123456789
refran14="El hombre no puede encontrar un lugar mas tranquilo que su propia alma"
print("Refran14: ", refran14)
print(refran14.find("lugar"),"=",refran14.index("lugar"))               # Devuelve 32 = 32
print(refran14.index("no")*refran14.index("b"))                         # Devuelve 60


# Ejercicio 15
#                  10        20        30        40        50        60        70
#         01234567890123456789012345678901234567890123456789012345678901234567890123456
refran15="El odio no deberia tener espacio en tu alma, pues eso no traera nada positivo"
print("Refran15: ", refran15)
print(refran15.find(", pues")//refran15.find("a t"))          # Devuelve 2
print(refran15.index("positivo"))                             # Devuelve 69
