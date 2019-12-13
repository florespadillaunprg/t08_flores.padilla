# Ejercicio 01
cadena01="Nunca he engañado a mi mujer. No es ningún mérito: la amo."
cadena02="Aquello de lo que hablamos es tan evidente que es completamente oscuro, y es tan abierto que es absolutamente secreto"
# Comparar si la cadena01 > cadena02
print("cadena01" > "cadena02")     # Muestra False



# Ejercicio 02
texto01="Una cosa es la vida y otra la novela. Una cosa es la filosofía y otra el pensamiento"
texto02="La poesía fue un objeto de lujo, pero para nosotros; es un artículo de primera necesidad: No podemos vivir sin poesía"
# Comparar si el texto01 == texto02
print("texto01" == "texto02")      # muestra False



# Ejercicio 03
frase01="Un vaso medio vacío de vino es también uno medio lleno, pero una mentiras a medias, de ningún modo es una media verdad"
frase02="Yo sé que la poesía es imprescindible, pero no sé para qué"
# Comparar si la frase01 != frase02
print("frase01" != "frase02")       # Muestra True




#Ejercicio 04
pensamiento01="A menudo la sensualidad apresura el crecimiento del amor, de modo que la raíz queda débil y es fácil de arancar"
pensamiento02="No se puede poseer mayor gobierno, ni menor, que el de uno mismo"
# Comparar si el pensamiento01 < pensamiento02
print("pensamiento01" < "pensamiento02")      # Muestra True



#Ejercicio 05
oracion01="A menudo la sensualidad apresura el crecimiento del amor, de modo que la raíz queda débil y es fácil de arancar"
oracion02="No se puede poseer mayor gobierno, ni menor, que el de uno mismo"
# Comparar si la oracion01 >= oracion02
print("oracion01" >= "oracion02")        # Muestra False





# Ejercicio 06
palabras01="No cojas la cuchara con la mano izquierda"
palabras02="En el camino dejé una pierna, un pulmón y un trozo de hígado. Pero debo decir, justo en este momento, que fui feliz con cáncer. Lo recuerdo como una de las mejores épocas de mi vida"
# Comparar si las palabras01 <= palabras02
print("palabras01" <= "palabras02")      # Muestra True




# Ejercicio 07
inicio01="Cada vez que decimos; «No sé », nos cerramos la puerta de nuestra propia fuente de sabiduría, que es infinita"
inicio02="Quien tiene miedo tiene desgracia"
# Comparar inicio01 <= inicio02 or inicio01 >= inicio02
print("inicio01" <= "inicio02" or "inicio01" >= "inicio02")     #Muestra True


# Ejercicio 08
final01="Cuando os disculpáis o dais las gracias, lo ideal es hacerlo sin esperar a que los otros cambien"
final02="Abrid escuelas y se cerrarán cárceles"
# Comparar not(not(final01 == final02 and final01 != final02))
print(not(not("final01" == "final02" and "final01" != "final02")))       # Muestra False



# Ejercicio 09
comparacion01="Se necesita una determinada forma de excavar, un cierto tipo de arqueología interna, para llegar a descubrir nuestra totalidad, aunque esté muy bien cubierta bajo capas de opiniones, de cosas que nos gustan y nos disgustan y por la densa niebla de los pensamientos y hábitos inconscientes y automáticos, por no mencionar el dolor"
comparacion02="Hombre, hombre, no se puede vivir enteramente sin piedad"
# Comparar comparacion01 != comparacion02 and comparacion01 != comparacion02
print("comparacion01" != "comparacion02" and "comparacion01" != "comparacion02")     #Muestra True



# Ejercicio 10
f_celebre01="Aquel que instaura una dictadura y no mata a Bruto, o aquel que funda una república y no mata a los hijos de Bruto, sólo gobernará un corto tiempo"
f_celebre02="Hoy he sentido de nuevo una gran admiración por ti. Y lamento mucho que hasta hoy no me haya dado suficientemente cuenta de lo maravilloso que eres"
# Comparar f_celebre01 < 20 or f_celebre02 == f_celebre01
print("f_celebre01" < "20" or "f_celebre02" == "f_celebre01")   # Muestra False




# Ejercicio 11
refran01="Vivir de apariencias te hace esclavo de los demás"
refran02="No importa lo que hagas en la vida, hazlo con todo tu corazón"
# Comparar refran01 >= refran01 or refran02 and refran02 == refran02
print("refran01" == "refran01" or "refran02" and "refran02" == "refran02")   # Muestra True



# Ejercicio 12
oda01="Todo parece imposible, hasta que se hace"
oda02="Nunca discutas con un estúpido, te hará descender a su nivel y ahí te vencerá por experiencia"
# Comparar not("oda01" < "oda02" or "oda01" > "oda02")
print(not("oda01" < "oda02" or "oda01" > "oda02"))      # Muestra False


# Ejercicio 13
cancion01="Cuando hay una tormenta los pajaritos se esconden, pero las águilas vuelan más alto"
cancion02="Lo que sabemos es una gota de agua; lo que ignoramos es el océano"
# Comparar "cancion01" != "cancion02" and "cancion01" == "cancion02"
print("cancion01" != "cancion02" and "cancion01" == "cancion02")     # Muestra False




# Ejercicio 14
reflexion01="Sabemos lo que somos pero no lo que podemos llegar a ser"
reflexion02="Cuanto más se juzga, menos se ama"
# Comparar "reflexion01" == "reflexion02" or not("reflexion01" != "reflexion02")
print("reflexion01" == "reflexion02" or not("reflexion01" != "reflexion02"))     # Muestra False



# Ejercicio 15
subcadena01="Con nada se aprende tanto como con enseñar"
subcadena02="Un pueblo ignorante es instrumento ciego de su propia destrucción"
# Comparar not("subcadena01" < "subcadena02") or not("subcadena01" == "subcadena02")
print(not("subcadena01" < "subcadena02") or not("subcadena01" == "subcadena02"))    # Muestra True
