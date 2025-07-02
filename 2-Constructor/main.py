#Clase con inicializador
class Persona:

  gender_options = ["Masculino", "Femenino", "Otro"]
  is_alive = True
  
  def __init__(self, name, age, gender, height):
    self.name = name
    self.age = age
    self.gender = gender if gender in self.gender_options else "Otro"
    self.height = height

  def birthday(self):
    self.age += 1
    print(f"Feliz cumpleaños {self.name}! Ahora tienes {self.age} años")

  def grow(self, height):
    self.height += height
    print(f"Ahora mides {self.height} metros")

  def die(self):
    self.is_alive = False
    print(f"{self.name} ha fallecido")

# persona1 = Persona("Lucas", 17, "Masculino", 1.95)

# print("Nombre de la persona 2: ",persona1.name, 
#   ", Edad: ",persona1.age, 
#   ", Genero: ",persona1.gender, 
#   ", Altura: ",persona1.height)

# persona1.birthday()
# persona1.grow(0.05)


# print(persona1.is_alive)
# persona1.die()
# print(persona1.is_alive)

personas = []

while True:
  print("1. Agregar persona")
  print("2. Ver personas")
  print("3. Salir")
  opcion = int(input("Ingrese una opción: "))

  if opcion == 1:
    nombre = input("Ingrese el nombre de la persona: ")
    edad = int(input("Ingrese la edad de la persona: "))
    genero = input("Ingrese el genero de la persona: ")
    altura = float(input("Ingrese la altura de la persona: "))

    persona = Persona(nombre, edad, genero, altura)
    personas.append(persona)
  
  if opcion == 2:
    for persona in personas:
      print(f"Nombre: {persona.name}, Edad: {persona.age}, Genero: {persona.gender}, Altura: {persona.height}")

  if opcion == 3:
    break