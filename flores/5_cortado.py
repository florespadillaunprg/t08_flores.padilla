# Ejercicio 01
#               10        20        30        40        50        60
#      0123456789012345678901234567890123456789012345678901234567890123
msj01="no se puede poseer mayor gobierno, ni menor, que el de uno mismo"
print(msj01[::-1])     # Invertir la cadena
print(msj01[:])        # Muestra toda la cadena


# Ejercicio 02
#               10        20        30        40        50        60
#      0123456789012345678901234567890123456789012345678901234567890123456
msj02="en la vida hay algo peor que el fracaso: el no haber intentado nada"
print(msj02[61:52:-1])        # Muestra intentado invertido (odatnetni)
print(msj02[6:10])            # Muestra "vida"


# Ejercicio 03
#               10        20        30        40        50
#      012345678901234567890123456789012345678901234567890123
msj03="cada hombre puede mejorar su vida mejorando su actitud"
print(msj03[53:46:-1])         # Muestra actitud invertida(dutitca)
print(msj03[18:24])            # Muestra "mejora"


# Ejercicio 04
#               10        20        30        40        50        60
#      0123456789012345678901234567890123456789012345678901234567890123456789
msj04="es mas facil luchar por unos principios que vivir de acuerdo con ellos"
print(msj04[38:28:-1])           # Muestra principios invertido(soipicnirp)
print(msj04[:60:-1])             # Muestra con ellos invertido(solle noc)


# Ejercicio 05
#               10        20        30        40        50        60        70
#      012345678901234567890123456789012345678901234567890123456789012345678901
msj05="si eres paciente en un momento de ira, escaparas a cien dias de tristeza"
print(msj05[23:37])                          # Muestra momento de ira
print(msj05[8:16] + " != " + msj05[64:])     # Muestra paciente != triteza


# Ejercicio 06
#               10        20        30        40        50        60        70        80        90
#      01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567
msj06="las cosas mejores y mas bellas del mundo no se pueden ver ni tocar, se deben sentir con el corazon"
# Mostrar la cosa mas bella es el corazon
print(msj06[27:29]+" "+msj06[4:8]+" "+msj06[20:23]+" "+msj06[24:29]+" "+msj06[45:43:-1]+" "+msj06[88:90]+" "+msj06[91:])
print(msj06[39:34:-1])       # Muestra mundo invertido(odnum)


# Ejercicio 07
#               10        20        30        40        50        60        70        80        90       100
#      01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456
msj07="piensa como una reina, una reina nunca tiene miedo al fracaso, el fracaso es otro escalon hacia la grandeza"
print(msj07[54:61]+" y "+msj07[99:])        # Muestra fracaso y grandeza
print(msj07[31:26:-1]+" y "+msj07[49:44:-1])     # Muestra reina y fracaso ambos invertidos


# Ejercicio 08
#               10        20        30        40        50
#      012345678901234567890123456789012345678901234567890123456
msj08="no permitas que nadie diga que eres incapaz de hacer algo"
print(msj08[31:35]+" "+msj08[38:43]+" "+msj08[44:46]+" "+msj08[53:])     # Muestra eres capaz de algo
print(msj08[:2]+" "+msj08[3:10]+" "+msj08[34:31:-1]+" "+msj08[36:43])    # muestra no permita ser incapaz


# Ejercicio 09
#               10        20        30        40        50        60        70
#      01234567890123456789012345678901234567890123456789012345678901234567890123456
msj09="la historia no es una carga para la memoria sino una iluminacion para el alma"
print(msj09[36:43]+" "+msj09[53:60]+"da")          # Muestra memoria iluminada
print("(("+msj09[3:11]+" del "+msj09[73:]+"))")    # Muestra ((histoeria del alma))


# Ejercicio 10
#               10        20        30        40        50        60        70
#      0123456789012345678901234567890123456789012345678901234567890123456789012345
msj10="se necesita poco para hacer las cosas bien, pero menos aun para hacerlas mal"
print(msj10[71:63:-1])         # Muestra hacerlas invertidas
print(msj10[41:21:-1])         # Muestra la frase hacer las cosas bien toda invertida


# Ejercicio 11
#               10        20        30        40        50
#      012345678901234567890123456789012345678901234567890123
msj11="es duro fracasar, pero es peor nunca haberlo intentado"
print(msj11[18:22]+" (es diferente de) "+msj11[26:30])    # Muestra pero (es diferente de) peor
print(msj11[15:7:-1])                                     # Muestra fracasar ivertida


# Ejercicio 12
#               10        20        30        40        50        60        70        80        90       100
#      01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
msj12="el hombre que mas ha vivido no es aquel que mas anios ha cumplido, sino aquel que mas ha experimentado la vida"
print(msj12[101:88:-1])       # Muestra experimentado invertido
print(msj12[103:105]+" "+msj12[106:]+" "+msj12[32:30:-1]+" "+msj12[89:100])       # Muestra la vida se experimenta


# Ejercicio 13
#               10        20        30        40        50        60        70        80
#      01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678
msj13="el exito es mas a menudo alcanzado por aquellos que no saben que el fracaso es inevitable"
print(msj13[42:44]+" "+msj13[3:8]+" "+msj13[9:11]+" mejor que el "+msj13[68:75])   # Muestra el exito es mejor que el fracaso
print(msj13[88:78:-1])       # Muestra inevitable invertida


# Ejercicio 14
#               10        20        30        40        50        60        70        80        90       100       110
#      01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789013234
msj14="la razon principal por la que las personas fracasan en la vida es porque escuchan a sus amigos, familiares y vecinos"
print("\'Yo tengo "+msj14[88:]+"\'")   # Muestra 'Yo tengo amigos, familiares y vecinos'
print(msj14[61:57:-1])                 # Muestra vida invertida


# Ejercicio 15
#               10        20        30        40        50        60        70        80        90
#      01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901
msj15="el exito no es definitivo, el fracaso no es fatal: lo que cuenta es el coraje para continuar"
# Mostra Para alcanzar el "exito" se necesita tener 'coraje'
print("Para alcanzar el \""+msj15[3:8]+"\" se  necesita tener \'"+msj15[71:77]+"\'")
print("\"\'"+msj15[30:37]+" "+msj15[44:49]+"\"\'")     # Muestra "'fracaso fatal"'
