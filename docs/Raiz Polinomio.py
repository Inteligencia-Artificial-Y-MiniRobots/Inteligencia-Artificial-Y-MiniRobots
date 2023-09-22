import random

# Definimos el polinomio P(x)
def P(x):
    return 5*x**5 - 3*x**4 - x**3 - 5*x**2 - x - 3

# Función para inicializar la población
def inicializar_poblacion(tamano_poblacion):
    poblacion = []
    for _ in range(tamano_poblacion):
        x = random.uniform(0.5,1)
        poblacion.append(x)
    return poblacion

# Función de clasificación basada en la diferencia absoluta
def clasificar_poblacion(poblacion):
    clasificacion = [(x, abs(P(x))) for x in poblacion]
    clasificacion.sort(key=lambda x: x[1])
    return [x[0] for x in clasificacion]

# Función de cruce por posición
def cruce_por_posicion(padre1, padre2):
    punto_cruce = random.randint(1, 4)
    hijo1 = padre1 if random.random() < 0.5 else padre2
    hijo2 = padre2 if hijo1 == padre1 else padre1
    return hijo1, hijo2

# Algoritmo genético para encontrar la raíz
def algoritmo_genetico(tamano_poblacion, num_generaciones):
    poblacion = inicializar_poblacion(tamano_poblacion)

    for _ in range(num_generaciones):
        poblacion = clasificar_poblacion(poblacion)
        nueva_generacion = []

        # Elitismo: mantenemos al mejor individuo de la generación anterior
        nueva_generacion.append(poblacion[0])

        # Cruce y mutación
        while len(nueva_generacion) < tamano_poblacion:
            padre1 = random.choice(poblacion)
            padre2 = random.choice(poblacion)
            hijo1, hijo2 = cruce_por_posicion(padre1, padre2)
            nueva_generacion.extend([hijo1, hijo2])

        poblacion = nueva_generacion

    # Devolvemos el mejor individuo de la última generación
    return clasificar_poblacion(poblacion)[0]

# Parámetros del AG
tamano_poblacion = 100
num_generaciones = 5000

# Ejecutamos el algoritmo genético
mejor_individuo = algoritmo_genetico(tamano_poblacion, num_generaciones)

print(f"La raíz aproximada es: {mejor_individuo}")