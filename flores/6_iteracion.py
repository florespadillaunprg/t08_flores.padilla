# Ejercicio 01
cadena01="Ni yo estoy en el mundo para cumplir tus expectativas ni tu estas en el mundo para cumplir las mias"
print("Cadena01: ",cadena01)

contador_a=0
contador_e=0
contador_i=0
contador_o=0
contador_u=0

for letra in cadena01:
    if (letra == 'a'):
        contador_a+=1
    if (letra == 'e'):
        contador_e+=1
    if (letra == 'i'):
        contador_i+=1
    if (letra == 'o'):
        contador_o+=1
    if (letra == 'u'):
        contador_u+=1

# Contar cuantas vocales existen en la cadena01
print("A: ",contador_a)   # devuelve 9
print("E: ",contador_e)   # devuelve 8
print("I: ",contador_i)   # devuelve 6
print("O: ",contador_o)   # devuelve 4
print("U: ",contador_u)   # devuelve 6


# Ejercicio 02
cadena02="El pesimista se queja del viento, el optimista espera que cambie, el realista ajusta las velas"
print("Cadena02: ",cadena02)

contador_r=0
contador_p=0

for letra in cadena02:
    if (letra == "r"):
        contador_r+=1
    if (letra == "p"):
        contador_p+=1

# Contar cuantas letras "r" y "pE existen en la cadena02
print("r: " , contador_r)    # Devuelve 2
print("p: ", contador_p)     # Devuelve 3


# Ejercicio 03
cadena03="Pedir perdon es de inteligentes, perdonar es de nobles pero perdonarse es de sabios"
print("Cadena03: ",cadena03)

contador_s=0
contador_n=0
contador_g=0

for letra in cadena03:
    if (letra == "s"):
        contador_s+=1
    if (letra == "n"):
        contador_n+=1
    if (letra == "g"):
        contador_g+=1

# Contar cuantas letras "s", "n", y "g" , esxisten en la cadena03
print("s: ", contador_s)      # Devuelve 8
print("n: ", contador_n)      # Devuelve 6
print("g: ", contador_g)      # Devuelve 1


# Ejercicio 04
cadena04="La reflexion es el camino hacia la inmortalidad"
print("Cadena04: ",cadena04)

contador_m=0
contador_n=0
contador_x=0

for letra in cadena04:
    if (letra == "m"):
        contador_m+=1
    if (letra == "n"):
        contador_n+=1
    if (letra == "x"):
        contador_x+=1

# Calcular cuantas letras "m", "n" y "x" , existen en la cadena04
print("m: ", contador_m)     # Devuelve 3
print("n: ", contador_n)     # Devuelve 2
print("x: ", contador_x)     # Devuelve 1


# Ejercicio 05
cadena05="Nunca podras plantar un buen futuro si estas anclado en el pasado"
print("Cadena05: ",cadena05)

contador_c=0
contador_b=0
contador_d=0

for letra in cadena05:
    if (letra == "c"):
        contador_c+=1
    if (letra == "b"):
        contador_b+=1
    if (letra == "d"):
        contador_d+=1

# Contar cuantas letras "c", "b" y "d", existen en la cadena05 y sumarlas
print("c: ", contador_c)    # Devuelve 2
print("b: ", contador_b)    # Devuelve 1
print("d: ", contador_d)    # Devuelve 3

suma=(contador_c + contador_b + contador_d)
print("Suma: ", suma)       # Devuelve 6

# Ejercicio 06
cadena06="No vas a encontrar una vida que valga la pena vivir, tienes que construirla tu mismo"
print("Cadena06: ",cadena06)

contador_l=0
contador_q=0

for letra in cadena06:
    if (letra == "l"):
        contador_l+=1
    if (letra == "q"):
        contador_q+=1

# Contar cuantas palabras "la" y "que" existen en la cadena06
print("l: ", contador_l)     # Devuelve 3
print("q: ", contador_q)     # Devuelve 2


# Ejercicio 07
cadena07="La vida es una sucesion de lecciones que uno debe vivir para entender"
print("Cadena07: ", cadena07)

contador_espacio=0
contador_comas=0

for letra in cadena07:
    if (letra == " "):
        contador_espacio+=1
    if (letra == ","):
        contador_comas+=1

# Contar cuantos espacios y cuantas comas existen en la cadena07
print("espacios: ", contador_espacio)    # Devuelve 12
print("comas: ", contador_comas)         # Devuelve 0


# Ejercicio 08
cadena08="Un dia de preocupacion en la vida es mucho mas agotador que una semana de trabajo"
print("Cadena08: ", cadena08)

contador_h=0
contador_t=0
contador_j=0

for letra in cadena08:
    if (letra == "h"):
        contador_h+=1
    if (letra == "t"):
        contador_t+=1
    if (letra == "j"):
        contador_j+=1

# Contar cuantas letras "h" , "t" y "j" , existen en la cadena08
print("h: ", contador_h)    # Devuelve 1
print("t: ", contador_t)    # Devuelve 2
print("j: ", contador_j)    # Devuelve 1


# Ejercicio 09
cadena09="si te tomas la vida demasiado enserio, nunca vas a salir vivo de ella"
print("Cadena09: ", cadena09)

contador_v=0
contador_s=0

for letra in cadena09:
    if (letra == "v"):
        contador_v+=1
    if (letra == "s"):
        contador_s+=1

# Contar cuantas letras "v" y "s" , existen en la cadena09
print("v: ", contador_v)     # Devuelve 4
print("s: ", contador_s)     # Devuelve 6


# Ejercicio 10
cadena10="El mejor espejo de la vida es un viejo amigo"
print("Cadena10: ", cadena10)

contador_E=0
contador_o=0

for letra in cadena10:
    if (letra == "E"):
        contador_E+=1
    if (letra == "o"):
        contador_o+=1

# Contar cuantas letras "E" hay y contar cuantas letras existen en la cadena
print("E: ", contador_E)           # Devuelve 1
print("o: ", contador_o)        # Devuelve 4


# Ejercicio 11
cadena11="La diferencia entre el fracaso y el exito reside en la voluntad del corazon"
print("Cadena11: ", cadena11)

contador_e=0
contador_a=0
contador_z=0

for letra in cadena11:
    if (letra == "e"):
        contador_e+=1
    if (letra == "a"):
        contador_a+=1
    if (letra == "z"):
        contador_z+=1

# Contar cuantas vocales "a" y "e", y letras "z" existen el la cadena11
print("e: ", contador_e)         # Devuelve 11
print("a: ", contador_a)         # Devuelve 7
print("z: ", contador_z)         # Devuelve 1


# Ejercicio 12
cadena12="Un hombre que no se alimenta de sus suenos es un hombre que envejece pronto"
print("Cadena12: ", cadena12)

contador_n=0
contador_U=0
contador_m=0

for letra in cadena12:
    if (letra == "n"):
        contador_n+=1
    if (letra == "U"):
        contador_U+=1
    if (letra == "m"):
        contador_m+=1

# Contar cuantas letras "n", "m" y vocal "U" existen en la cadena12
print("n: ", contador_n)      # Devuelve 13
print("U: ", contador_U)      # Devuelve 1
print("m: ", contador_m)      # Devuelve 3


# Ejercicio 13
cadena13="No hay vida mas completa que aquella que puedes vivir por eleccion propia"
print("Cadena13: ", cadena13)

contador_c=0
contador_v=0
contador_p=0

for letra in cadena13:
    if (letra == "c"):
        contador_c+=1
    if (letra == "v"):
        contador_v+=1
    if (letra == "p"):
        contador_p+=1

# Contar cuantas letras "c" , "v" y "p" existen el la cadena13
print("c: ", contador_c)        # Devuelve 3
print("v: ", contador_v)        # Devuelve 3
print("p: ", contador_p)        # Devuelve 5


# Ejercicio 14
cadena14="La calidad de la vida de una persona es directamente proporcional a su compromiso con la excelencia. No importa a que se dedique"
print("Cadena14: ", cadena14)

contador_puntos=0
contador_r=0
contador_punto_y_coma=0

for letra in cadena14:
    if (letra == "."):
        contador_puntos+=1
    if (letra == "r"):
        contador_r+=1
    if (letra == ";"):
        contador_punto_y_coma+=1

# Contar cuantas letras "r", puntos y puntos y coma existen en la cadena14
print("puntos: ", contador_puntos)               # Devuelve 1
print("r: ", contador_r)                         # Devuelve 6
print("punto y  coma: ", contador_punto_y_coma)  # Devuelve 0


# Ejercicio 15
cadena15="La vida tiene valor siempre que se valore la vida de los otros, a traves del amor, la amistad, la indignacion y la compasion"
print("Cadena15: ", cadena15)

contador_coma=0
contador_v=0
contador_i=0
contador_L=0
contador_n=0

for letra in cadena15:
    if (letra == ","):
        contador_coma+=1
    if (letra == "v"):
        contador_v+=1
    if (letra == "i"):
        contador_i+=1
    if (letra == "L"):
        contador_L+=1
    if (letra == "n"):
        contador_n+=1

# Contar cuantas letras "v", "L", "n" , vocal "i" y comas existen en la cadena15
print("comas: ", contador_coma)   # Devuelve 3
print("v: ", contador_v)          # Devuelve 5
print("i: ", contador_i)          # Devuelve 9
print("L: ", contador_L)          # Devuelve 1
print("n: ", contador_n)          # Devuelve 5
