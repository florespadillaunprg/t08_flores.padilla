# Ejercicio 01
nombre="Alex"
escuela="I. E. San Juan"
curso="Matemática"

mensaje=nombre + " estudia " + curso + " en la " + escuela
print(mensaje)


# Ejercicio 02
cliente="Jose"
producto="arroz"
precio=4

# Si el precio del producto es mayor que 4, Jose no comprara el producto
if(precio > 4):
    msj=nombre + " compro el " + producto
else:
    msj=nombre + " no compro el " + producto
# Fin_if
print(msj)


# Ejercicio 03
universidad="Pedro Ruiz Gallo"
alumno="Pedro"
ciudad="Chiclayo"

informacion=alumno + " estudia en la Universidad Nacional "+ universidad + "en la ciudad de "+ ciudad
print(informacion)


# Ejercicio 04
estudiante="Paolo"
asignatura="Matematicas"
promedio_general=13

# Si la nota es mayor a 10.5, Paolo desaprobara la asignatura de matematicas
if (promedio_general>10.5):
    situcion_final=estudiante + " no desaprobara " + asignatura
else:
    situcion_final=estudiante + " desaprobara " + asignatura
# Fin_if
print(situcion_final)


# Ejercicio 05
comprador="Lucas"
celular="Samsumg"
precio_celular=800.56

# Si el precio del celular es mayor a 700, Lucas no comprara el celular
if (precio_celular>700):
    venta=comprador + " no compro su celular "+ celular
else:
    venta=comprador + " compro su celular " + celular
# Fin_if
print(venta)


# Ejercicio 06
vendedor="Casemiro"
bodega="LA CHICLAYANITA"
productos_vencidos=43

# Si los productos vencidos superan los 50, Casemiro ira a la carcel
if (productos_vencidos>50):
    libertad="En la bodega "+bodega+" de don "+vendedor+" se encontraron productos vencidos, por lo tanto ira a la carcel"
else:
    libertad="En la bodega "+bodega+ " de don "+vendedor+" no se encontaron productos vencidos, por lo tanto no ira a la carcel"
# Fin_if
print(libertad)


# Ejercicio 07
amigo="Fernando"
horas="5"
distrito="La Victoria"

descenlace="La casa de "+ amigo+ " esta a "+horas+ " horas del distrito "+ distrito
print(descenlace)


# Ejercicio 08
departamento="Lima"
temperatura=40.36

# Si la temperatura pasa los 60.5°, todas las personas de lima moriran, caso contrario, todas las personas estaran salvadas
if(temperatura>60.5):
    anuncio="Todas las personas del departamento de "+ departamento+ " moriran."
else:
    anuncio="Todas las personas del departamento de "+ departamento+ " estan salvadas."
# Fin_if
print(anuncio)


# Ejercicio 09
abuela="Maria"
musica="huaynos"
cumpleanios="14 de febrero"

revelacion="Mi abuela "+abuela+ " baila "+musica+ " en sus cumpleaños todos los "+cumpleanios
print(revelacion)


# Ejercicio 10
mujer="Teresa"
varon="Manuel"
amor="Infinito"

s_sentimental=varon+ " y "+ mujer + " se declararon amor "+ amor
print(s_sentimental)


# Ejercicio 11
tia="Francisca"
hijos="2"
edad=35

# Si la edad de Francisca supera los 40 años, ella  no seguira teniendo posibilidad de tener un tercer bebe
if(edad>40):
    resultado="Mi tia "+tia+ " seguira teniendo "+hijos+ " hijos"
else:
    resultado="Mi tia "+tia+ " sigue teniendo posiblidad de tener un tercer hijo"
# Fin_if
print(resultado)


# Ejercicio 12
abuelita="Josefina"
abuelito="Gabriel"
anios_de_casados=53

# Si los años de casados de mis abuelitos superan las 51 años, celebraran bodas de oro, de lo contrario, no.
if(anios_de_casados>51):
    bodas_oro="Mis abuelitos "+abuelito+" y "+abuelita+ " celebraran sus boda de oro"
else:
    bodas_oro="Mis abuelitos "+abuelito+" "+abuelita+" celebraran boda de plata"
# Fin_if
print(bodas_oro)


# Ejercicio 13
hotel="DESCANSA TRANQUILO Y SEGURO"
habitaciones=20

# Los jugadores de barcelona descansaran en el hotel si hay mas de 30 habitaciones
if ( habitaciones>30):
    final="Los jugadores de barcelona descansaran en el hotel \'"+hotel+ "\'"
else:
    final="Los jugadores de barcelona abandonaran el hotel \'"+hotel+"\'"
# Fin_if
print(final)


# Ejercicio 14
club="Universitario"
jugadores=21

# Si el club universitario tiene mas de 30 jugadores, entonces jugaran la primera division;y si no los tiene, jugaran la segunda division
if (jugadores>30):
    plantel="El club \""+club+"\" juagara la primera division"
else:
    plantel="El club \""+ club +"\" jugara la segunda division"
# Fin_if
print(plantel)


# Ejercicio 15
pais="Estados Unidos"
paises=35

# Si la cantidad de paise es mayor a 30 se desarrollara la tercera guerra mundial, y si no , se desarrollara una guera continental
if(paises>30):
    tipo_guerra=pais + " anucio esta mañana que habra guerra mundial"
else:
    tipo_guerra=pais + " anuncion esta mañana que habra guerra continental"
# Fin_if
print(tipo_guerra)
