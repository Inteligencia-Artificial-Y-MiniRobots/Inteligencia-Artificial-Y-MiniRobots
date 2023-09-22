import random

# Definir datos del problema
plantas = ['Cali', 'Bogotá', 'Medellín', 'Barranquilla']
ciudades = ['Cali', 'Bogotá', 'Medellín', 'Barranquilla']
capacidades = [3, 6, 5, 4]
demandas = [4, 3, 5, 3]
transporte = [[1, 4, 3, 6], [4, 1, 4, 5], [3, 4, 1, 4], [6, 5, 4, 1]]
costos_generacion = {'Cali': 680, 'Bogotá': 720, 'Medellín': 660, 'Barranquilla': 750}

# Definir funciones auxiliares
def costo_total(asignacion):
    costo_transporte = 0
    costo_generacion = 0
    for i in range(len(asignacion)):
        planta = asignacion[i]
        ciudad = ciudades[i]
        costo_transporte += transporte[plantas.index(planta)][ciudades.index(ciudad)]
        costo_generacion += capacidades[plantas.index(planta)] * costos_generacion[planta]
    return costo_transporte + costo_generacion

def generar_poblacion_inicial(tamano_poblacion):
    poblacion = []
    for _ in range(tamano_poblacion):
        individuo = [random.choice(plantas) for _ in range(len(ciudades))]
        poblacion.append(individuo)
    return poblacion

def seleccion(poblacion):
    return min(poblacion, key=costo_total)

def cruce(padre1, padre2):
    punto_cruce = random.randint(1, len(padre1) - 1)
    descendiente1 = padre1[:punto_cruce] + padre2[punto_cruce:]
    descendiente2 = padre2[:punto_cruce] + padre1[punto_cruce:]
    return descendiente1, descendiente2

def mutacion(individuo, probabilidad_mutacion):
    for i in range(len(individuo)):
        if random.random() < probabilidad_mutacion:
            individuo[i] = random.choice(plantas)
    return individuo

# Definir parámetros del algoritmo
tamano_poblacion = 100
probabilidad_mutacion = 0.1
num_generaciones = 1000

# Inicializar población
poblacion = generar_poblacion_inicial(tamano_poblacion)

# Ciclo de optimización
for _ in range(num_generaciones):
    poblacion = sorted(poblacion, key=costo_total)[:tamano_poblacion]
    padre1 = seleccion(poblacion)
    padre2 = seleccion(poblacion)
    descendiente1, descendiente2 = cruce(padre1, padre2)
    descendiente1 = mutacion(descendiente1, probabilidad_mutacion)
    descendiente2 = mutacion(descendiente2, probabilidad_mutacion)
    poblacion.extend([descendiente1, descendiente2])

# Obtener la mejor asignación
mejor_asignacion = seleccion(poblacion)
mejor_costo = costo_total(mejor_asignacion)

print("Mejor asignación de generadores a ciudades:")
for i in range(len(ciudades)):
    print(f"{ciudades[i]} -> {mejor_asignacion[i]}")
print(f"Costo total: {mejor_costo}")
