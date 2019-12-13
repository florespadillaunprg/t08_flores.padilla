# Ejercicio 01
cadena01="Puede que nos quiten la vida, pero jamas nos quitaran la libertad"
cadena02="Los exitos mas importantes se consiguen cuando existe la posibilidad de fracasar"
# Comparar si la cadena01 > cadena02
print("cadena01" > "cadena02")     # Devuelve False


# Ejercicio 02
texto01="La educacion es el arma mas poderosa que puedes usar para cambiar el mundo"
texto02="Solo cabe progresar cuando se piensa en grande, sólo es posible avanzar cuando se mira lejos"
# Comparar si el texto01 == texto02
print("texto01" == "texto02")      # Devuelve False


# Ejercicio 03
frase01="Los dos guerreros mas poderosos son la paciencia y el tiempo"
frase02="Arder de deseo y guardar silencio es el mayor castigo que podemos imponernos a nosotros mismos"
# Comparar si la frase01 != frase02
print("frase01" != "frase02")       # Devuelve True


#Ejercicio 04
pensamiento01="No debeis temer a la muerte; desafiadla, y llevareis el miedo a las nuestros enemigos"
pensamiento02="Es mejor ser conocido por todo el mundo, incluso por ser una estrella del sexo, que no ser conocido en absoluto"
# Comparar si el pensamiento01 < pensamiento02
print("pensamiento01" < "pensamiento02")      # Devuelve True


# Ejercicio 05
oracion01="La ciencia es un hermoso regalo para la humanidad; no debemos distorsionarlo"
oracion02="Viajar es un ejercicio con consecuencias fatales para los prejuicios, la intolerancia y la estrechez de mente"
# Comparar si la oracion01 >= oracion02
print("oracion01" >= "oracion02")        # Devuelve False


# Ejercicio 06
palabras01="Solo dos cosas son infinitas, el universo y la estupidez humana, y no estoy seguro de la primera"
palabras02="Si rechazas la comida, ignoras la vestimenta, temes la religion y evitas a las personas, quizas sea mejor que te quedes en casa"
# Comparar si las palabras01 <= palabras02
print("palabras01" <= "palabras02")      # DEvuelve True


# Ejercicio 07
inicio01="Es extrano que solo hombres extraordinarios hagan los descubrimientos, que luego parecen tan faciles y simples"
inicio02="El instinto mas grande de los ninos es precisamente liberarse del adulto"
# Comparar inicio01 <= inicio02 or inicio01 >= inicio02
print("inicio01" <= "inicio02" or "inicio01" >= "inicio02")     #Devuelve True


# Ejercicio 08
final01="La ciencia sin religion esta coja, la religion sin ciencia esta ciega"
final02="La naturaleza te da la cara que tienes a los veinte anios. Depende de ti merecer la cara que tienes a los cincuenta"
# Comparar not(not(final01 == final02 and final01 != final02))
print(not(not("final01" == "final02" and "final01" != "final02")))       # Devuelve False


# Ejercicio 09
comparacion01="No le puedes ensenar nada a un hombre; solo puedes ayudarlo a descubrirlo por si mismo"
comparacion02="La forma en que hablamos a nuestros hijos se convierten en su voz interior"
# Comparar comparacion01 != comparacion02 and comparacion01 != comparacion02
print("comparacion01" != "comparacion02" and "comparacion01" != "comparacion02")     #Devuelve True


# Ejercicio 10
f_celebre01="Hay que tener un gran coraje para oponerse a nuestros enemigos, pero hace falta mas valor aun para hacerlo con los amigos"
f_celebre02="Si no te gusta el camino que estas caminando, inicia la pavimentacion de otro"
# Comparar f_celebre01 < 20 or f_celebre02 == f_celebre01
print("f_celebre01" < "20" or "f_celebre02" == "f_celebre01")   # Devuelve True


# Ejercicio 11
refran01="Todo gran poder conlleva una gran responsabilidad"
refran02="Tenemos que ser menos curiosos por la gente y mas tener más curiosidad por las ideas"
# Comparar refran01 >= refran01 or refran02 and refran02 == refran02
print("refran01" == "refran01" or "refran02" and "refran02" == "refran02")   # Devuelve True


# Ejercicio 12
oda01="La flor que crece en la adversidad es la mas hermosa de todas"
oda02="Un libro abierto es un cerebro que habla; cerrado, es un amigo que espera"
# Comparar not("oda01" < "oda02" or "oda01" > "oda02")
print(not("oda01" < "oda02" or "oda01" > "oda02"))      # Devuelve False


# Ejercicio 13
cancion01="La educacion es el pasaporte hacia el futuro, el manana pertenece a aquellos que se preparan para el en el dia de hoy"
cancion02="La musica puede cambiar el mundo porque puede cambiar a la gente"
# Comparar "cancion01" != "cancion02" and "cancion01" == "cancion02"
print("cancion01" != "cancion02" and "cancion01" == "cancion02")     # Devuelve False


# Ejercicio 14
reflexion01="El exito tiene muchos padres, pero el fracaso es huerfano"
reflexion02="Recuerda que el cuerpo es transitorio, pero el alma perdura en la eternidad"
# Comparar "reflexion01" == "reflexion02" or not("reflexion01" != "reflexion02")
print("reflexion01" == "reflexion02" or not("reflexion01" != "reflexion02"))     # Devuelve False


# Ejercicio 15
subcadena01="El secreto de la existencia humana no solo esta en vivir, sino tambien en saber para que se vive"
subcadena02="La pobreza de bienes es facilmente remediable, mas la del alma es irreparable"
# Comparar not("subcadena01" < "subcadena02") or not("subcadena01" == "subcadena02")
print(not("subcadena01" < "subcadena02") or not("subcadena01" == "subcadena02"))    # Devuelve True
