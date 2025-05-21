class Habitacion:
    def __init__(self, numero, tipo, precio_noche, disponible):
        self.numero = numero
        self.tipo = tipo
        self.precio_noche = precio_noche
        self.disponible = disponible

class Cliente:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

class Reserva:
    def __init__(self, habitacion, cliente, noches):
        self.habitacion = habitacion
        self.cliente = cliente
        self.noches = noches

def mostrar_habitaciones_disponibles(habitaciones):
    print("Habitaciones disponibles:")
    for habitacion in habitaciones:
        if habitacion.disponible:
            print(f"Número: {habitacion.numero}, Tipo: {habitacion.tipo}, Precio por noche: {habitacion.precio_noche}")

def hacer_reserva(habitaciones, numero, cliente, noches):
    for habitacion in habitaciones:
        if habitacion.numero == numero and habitacion.disponible:
            if noches <= 0:
                print("La cantidad de noches debe ser mayor a cero.")
                return
            habitacion.disponible = False
            reserva = Reserva(habitacion, cliente, noches)
            print(f"Reserva realizada para {cliente.nombre} {cliente.apellido}.")
            print(f"Habitación {habitacion.numero} por {noches} noches.")
            return
    print("Habitación no disponible o número incorrecto.")

def main():
    habitaciones = [
        Habitacion(101, "Individual", 50, True),
        Habitacion(102, "Doble", 80, True),
        Habitacion(201, "Suite", 120, True)
    ]

    opcion = input("1. Ver habitaciones disponibles\n2. Reservar habitación\nSeleccione una opción: ")

    if opcion == '1':
        mostrar_habitaciones_disponibles(habitaciones)
    elif opcion == '2':
        n = input("Nombre: ")
        a = input("Apellido: ")
        dni = input("DNI: ")
        cliente = Cliente(n, a, dni)

        numero = int(input("Número de habitación: "))
        noches = int(input("Número de noches: "))
        hacer_reserva(habitaciones, numero, cliente, noches)
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
