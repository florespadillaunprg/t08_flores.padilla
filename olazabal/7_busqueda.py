# Ejercicio 01
#                  10        20        30
#         012345678901234567890123456789012345
refran01="Al buen amar, nunca le falta que dar"
print("Refran 01: ", refran01)
print(refran01.find("nunca"))         # Devuelve 14
print(refran01.index("le"))           # Devuelve 20


# Ejercicio 02
#                  10        20        30        40        50        60        70        80
#         01234567890123456789012345678901234567890123456789012345678901234567890123456789012345
refran02="El tiempo me enseño que el alimento del amor, es la confianza, el respeto y un colchón"
print("Refran 02: ",refran02)
# Devolver codigo 1234
print(refran02.find("l"),refran02.find(" "),refran02.find("t"),refran02.find("i"))


# Ejercicio 03
#                   10        20        30        40
#         012345678901234567890123456789012345678901234
refran03="Amor por interés, se acaba en un dos por tres"
print("Refran 03: ", refran03)
# Devolver numeros 9 12 30 3
print(refran03.index("i"),refran03.index("e"),refran03.index("u"),refran03.index("r"))


# Ejercicio 04
#                   10        20        30        40        50        60
#         012345678901234567890123456789012345678901234567890123456789012345678
refran04="Hay tres cosas que no se pueden ocultar: el humo, el amor y el dinero"
print("Refran 04: ", refran04)
# Devolver 56 68 0 verticalmente
print(refran04.index("r y"))   # Devuelve 56
print(refran04.find("o"))      # Devuelve 68
print(refran04.find("H"))      # Devuelve 0


# Ejercicio 05
#                  10        20        30
#         01234567890123456789012345678901234
refran05="Quien bien te quiere te hará llorar"
print("Refran 05: ", refran05)
print(refran05.index("te"))        # Devuelve 11
print(refran05.find("bien"))       # Devuelve 6


# Ejercicio 06
#                   10        20        30
#         0123456789012345678901234567890123456
refran06="A amor y fortuna, resistencia ninguna"
print("Refran06: ", refran06)
print(refran06.find("for"))          # Devuelve 9
print(refran06.index("cia"))         # Devuelve 26

# Ejercicio 07
#                   10        20        30        40        50        60
#         0123456789012345678901234567890123456789012345678901234567890
refran07="El que tiene un novio en Granada ni tiene novio ni tiene nada"
print("Refran 07: ", refran07)
print(refran07.index("ada"))         # Devuelve 58
print(refran07.find("vio"))          # Devuelve 18


# Ejercicio 08
#                   10        20        30
#         012345678901234567890123456789012345678901
refran08="El sexo alivia la tensión. El amor la crea"
print("Refran08: ", refran08)
print(refran08.index("crea"))        # Devuelve 38
print(refran08.find("sión"))         # Devuelve 21


# Ejercicio 09
#                   10        20        30        40
#         01234567890123456789012345678901234567890123456
refran09="Si al amor le haces caso, es seguro el embarazo"
print("Refran 09: ", refran09)
print(refran09.index("embarazo"),":" ,refran09.find("so"))       # Devuelve 39 : 22


# Ejercicio 10
#                   10        20        30        40
#         01234567890123456789012345678901234567890123456
refran10="El que ama a una casada, puede morir de cornada"
print("Refran 10: ", refran10)
print(refran10.index("ada"),",",refran10.find("puede"),"y",refran10.index("ama"))      # Devuelve 20 , 25 y 7


# Ejercicio 11
#                  10        20        30        40        50        60
#         0123456789012345678901234567890123456789012345678901234567890123
refran11="La que de treinta no tiene novio, tiene un humor como un demonio"
print("Refran 11: ", refran11)
print(refran11.index("qu"))          # Devuelve 3
print(refran11.index("no"))          # Devuelve 18


# Ejercicio 12
#                  10        20        30        40        50
#         01234567890123456789012345678901234567890123456789012345
refran12="Quien promete amor eterno es porque desconoce los cuernos"
print("Refran 12: ", refran12)
print(refran12.find(" p"))                                                          # Devuelve 55
print(refran12.index("s p"),"-",refran12.find("amor"),"=",refran12.find(" "))      # Devuelve 27 - 14 =13


# Ejercicio 13
#                   10        20        30
#         012345678901234567890123456789012345678
refran13="Si me quiere, con esta cara; sino, vaya"
print("Refran 13: ", refran13)
print(refran13.find("S"))       # Devuelve 0
print(refran13.index(";"))      # Devuelve 27


# Ejercicio 14
#                   10        20        30
#         01234567890123456789012345678901234567
refran14="Con amor y aguardiente, nada se siente"
print("Refran 14: ", refran14)
print(refran14.find("y"),"=",refran14.index("y"))               # Devuelve 9 = 9
print(refran14.index("nada")*refran14.index("e"))              # Devuelve 432


# Ejercicio 15
#                   10        20        30        40        50
#         012345678901234567890123456789012345678901234567890
refran15="No hay otra cura para el amor más que el matrimonio"
print("Refran 15: ", refran15)
print(refran15.find("amor")//refran15.find("hay"))          # Devuelve 8
print(refran15.index("más"))                                # Devuelve 30
