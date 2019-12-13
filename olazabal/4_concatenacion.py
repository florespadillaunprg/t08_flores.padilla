# Ejercicio 01
comprador="Harry Potter"
celular="Xiomi GT4"
precio_celular=1799.99

# Si el precio del celular es mayor a 1000, Harry Potter no comprara el celular
if (precio_celular>1000):
    venta=comprador + " no compro el celular "+ celular
else:
    venta=comprador + " compro el celular " + celular
# Fin_if
print(venta)



# Ejercicio 02
cliente="Ron Weasly"
producto="barita magica"
precio=50.00

# Si el precio del producto es mayor que 30.99, Ron Weasly no comprará el producto
if(precio > 50.99):
    msj=cliente + " compro la " + producto
else:
    msj=cliente + " no compro la " + producto
# Fin_if
print(msj)




# Ejercicio 03
colegio="Hogwarts"
alumno="Remus Lupin"
ciudad="montañas cerca a un lago"

informacion=alumno + " estudia en el colegio "+ colegio + " de magia y hechiceria que se encuentra por unas "+ ciudad
print(informacion)



# Ejercicio 04
estudiante="Hermione Granger"
asignatura="Artes Oscuras"
promedio_general=17
# Si la nota es mayor a 10.5, Hermione Granger desaprobara la asignatura de Artes Oscuras
if (promedio_general>10.5):
    situcion_final=estudiante + " no desaprobara " + asignatura
else:
    situcion_final=estudiante + " desaprobara " + asignatura
# Fin_if
print(situcion_final)



# Ejercicio 05
nombre="Luna Lovegood"
escuela="Hogwarts"
curso="Adivinacion"

mensaje=nombre + " estudia " + curso + " en " + escuela
print(mensaje)



# Ejercicio 06
vendedor="Garrick Ollivander"
bodega="Ollivanders"
productos_vencidos=0

# Si los productos vencidos superan los 100, Ollivander ira a la Azkaban
if (productos_vencidos>100):
    libertad="En la bodega "+bodega+" de "+vendedor+" se encontraron baritas en mal estado, por lo tanto ira a la carcel"
else:
    libertad="En la bodega "+bodega+ " de "+vendedor+" no se encontaron baritas en mal estado, por lo tanto no ira a la carcel"
# Fin_if
print(libertad)



# Ejercicio 07
amigo="Rubeus Hagrid"
horas="2"
distrito="Hogwarts"

descenlace="La casa de "+ amigo+ " esta a "+horas+ " horas del colegio "+ distrito
print(descenlace)



# Ejercicio 08
pais="Gran Bretaña"
temperatura=40.36

# Si la temperatura pasa los 60.5°, todas las personas muggles de Gran Bretaña moriran, caso contrario, todas las personas de sangre pura estaran salvadas
if(temperatura>60.5):
    anuncio="Todas las personas muggles de "+ pais+ " moriran."
else:
    anuncio="Todas las personas de sangre pura de "+ pais+ " estan salvadas."
# Fin_if
print(anuncio)



# Ejercicio 09
mama="Molly Weasly "
musica="ranas"
cumpleanios="30 de Octubre"

revelacion="La mamá de Ron Weasly es "+mama+ " y le gusta escuchar a las "+musica+ " en sus cumpleaños todos los "+cumpleanios
print(revelacion)



# Ejercicio 10
mujer="LiLy Potter"
varon="James Potter"
amor="Infinito"

s_sentimental=varon+ " y "+ mujer + " se declararon amor "+ amor
print(s_sentimental)



# Ejercicio 11
tia="Petuna Dursley"
hijos="1"
edad=40

# Si la edad de Petuna Dursley supera los 40 años, ella  no seguira teniendo posibilidad de tener un segundo bebe
if(edad>40):
    resultado="La tia de Harry Potter "+tia+ " seguira teniendo "+hijos+ " hijos"
else:
    resultado="La tia de Harry Potter "+tia+ " sigue teniendo posiblidad de tener un segundo hijo"
# Fin_if
print(resultado)




# Ejercicio 12
chico="Artur Weasly"
chica="Molly Weasly"
anios_de_casados=56

# Si los años de casados de Artur y Molly superan las 51 años, celebraran bodas de oro, de lo contrario, no.
if(anios_de_casados>51):
    bodas_oro=chico+" y "+chica+ " celebraran sus boda de oro"
else:
    bodas_oro=chico+" y "+chica+ " celebraran sus boda de oro"
# Fin_if
print(bodas_oro)



# Ejercicio 13
casa="Gryffindor"
habitaciones=7

# Los jugadores de Quidditch descansaran en la casa de Gryffindor si hay mas de 30 habitaciones
if ( habitaciones>30):
    final="Los jugadores de Quidditch descansaran en la casa de \'"+casa+ "\'"
else:
    final="Los jugadores de Quidditch abandonaran la casa de \'"+casa+"\'"
# Fin_if
print(final)



# Ejercicio 14
club=" Equipo Nacional de Quidditch Búlgaro"
jugadores=12

# Si el club universitario tiene mas de 15 jugadores, entonces jugaran el mundial de Quidditch;y si no los tiene, serán descalificados
if (jugadores>30):
    plantel="El \""+club+"\" juagara el mundial de Quidditch"
else:
    plantel="El club \""+ club +"\" serán descalificados"
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



# Ejercicio 15
pais="Gran Bretaña"
paises=3

# Si la cantidad de paise es mayor a 2 se desarrollara la segunda guerra mundial, y si no , se desarrollara una guera por el poder de la sangre
if(paises>2):
    tipo_guerra=pais + " anucio esta mañana que habra una segunda guerra mundial"
else:
    tipo_guerra=pais + " anuncion esta mañana que habra guerra por el poder de la sangre"
# Fin_if
print(tipo_guerra)
