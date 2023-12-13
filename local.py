from queue import Queue
import time

inicio_programa = time.time()  # Guardamos el momento en que inicia el programa
print("Simulación de cola en cajero\n")

cola = Queue()
# Añadimos un mínimo de 7 personas a la cola antes de abrir el negocio
for i in range(1, 8):
    cola.put(i)

tiempo_total = 0  # Para llevar el tiempo total de atención
tiempo_atencion = 3  # Cada cliente toma 3 minutos en ser atendido
cliente_actual = 0  # Para rastrear el número del cliente actual

while True:
    tiempo_ejecucion = time.time() - inicio_programa  # Actualizamos el tiempo de ejecución
    tiempo_total_acumulado = tiempo_total + tiempo_ejecucion  # Sumamos el tiempo de ejecución al tiempo total

    print(f"\nTotal de clientes en cola: {cola.qsize()}")
    print(f"Tiempo total acumulado: {tiempo_total_acumulado:.2f} segundos")
    print("Menú:")
    print("1. Añadir una persona a la cola")
    print("2. Atender al siguiente cliente")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        persona = cola.qsize() + 1
        cola.put(persona)
        print(f"Persona {persona} añadida a la cola.")
    elif opcion == '2':
        if cola.empty():
            print("No hay más clientes en la cola.")
        else:
            cliente_actual += 1
            tiempo_cliente = tiempo_atencion
            cola.get()  # Removemos al cliente que está siendo atendido
            tiempo_total += tiempo_cliente
            print(f"Cliente {cliente_actual} atendido en {tiempo_cliente} minutos. Tiempo total de atención: {tiempo_total} minutos.")
    elif opcion == '3':
        break
    else:
        print("Opción no válida. Intente de nuevo.")

# Al final, después de atender a todos los clientes o decidir salir, mostramos el tiempo total acumulado.
tiempo_ejecucion_final = time.time() - inicio_programa
tiempo_total_acumulado_final = tiempo_total + tiempo_ejecucion_final
print(f"\nFin de la simulación. Tiempo total acumulado: {tiempo_total_acumulado_final:.2f} segundos.")
