# Esto es un comentario y sirve para dar contexto de que se hace, se hizo o se hara


edad = 30

# variables de texto


# si queremos tener un texto que pueda contener saltos de linea
descripcion = """hola amigos:
como estan?
yo muy bien jeje
"""



#print(descripcion2)


# variables numericas
year = 2022

# type() => mostrara que tipo de variable es
#print(type(year))



# en Python no hace validacion del tipo de dato primario (si la variable 'nace' siendo string) normal se puede cambiar su tipo a otro (Boolean, int, float, array, etc.)
# en Python no existen las constantes
dni= [123123123]
dni= 'peruano'
dni= False

# id() > dara la ubicacion de esa variablen en relacion a la memoria del dispositivo
print(id(dni))


print(type(especialidad))

mes, dia = "febrero", 28

print(mes)

# del > elimina la variable de la memoria 
del mes

# si queremos usar luego de la eliminacion esa variable no sera posible ya que se elimino de la memoria
print(mes)









#Variable de Texto


Perro = "Toby"


#Variables de print 

nombre = "Alicia"
edad = 35
print("Me llamo", nombre, "y tengo", edad, "años.")

#Variables numericas

a = 2
b = 3
c = a + b

#Variables String   

s = input("Ingresa tu tweet")
if len(s)>140:
  print("Este tweet es demasiado largo!")

