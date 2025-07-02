
#Clase Persona
class Persona:

  name = ""
  age = 0
  gender = ""
  height = 0.00

  def walk(self):
    return f"Soy {self.name} y estoy caminando..."


#---------------------------------
#Instancia de la clase Persona
persona1 = Persona()
persona2 = Persona()

persona1.name = "Juan"
persona1.age = 20
persona1.gender = "Masculino"
persona1.height = 1.75

persona2.name = "Maria"

print("Nombre de la persona 1: ",persona1.name, 
  ", Edad: ",persona1.age, 
  ", Genero: ",persona1.gender, 
  ", Altura: ",persona1.height)

print("Nombre de la persona 2: ",persona2.name, 
  ", Edad: ",persona2.age, 
  ", Genero: ",persona2.gender, 
  ", Altura: ",persona2.height)

print(persona1.walk())

