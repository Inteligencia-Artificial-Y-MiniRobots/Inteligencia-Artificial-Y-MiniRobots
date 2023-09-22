import random

# Definición de alimentos (nombre, calorías, proteínas, grasas, carbohidratos)
alimentos = [
    (Huevo, 68, 5.5, 4.8, 0.6),
    (Pollo, 165, 31, 3.6, 0),
    (Arroz, 130, 2.7, 0.3, 28),
    (Pasta, 131, 5.5, 0.5, 25),
    (Leche, 42, 3.4, 1, 4.8),
    (Atún, 128, 26, 1, 0),
    (Plátano, 105, 1.3, 0.3, 27),
    (Manzana, 95, 0.5, 0.3, 25),
    (Brócoli, 55, 3.7, 0.6, 11),
    (Zanahoria, 41, 0.9, 0.2, 10),
    (Nuez, 185, 4.3, 18.5, 3.9),
    (Aguacate, 160, 2, 14.7, 8.5),
    (Pan Integral, 69, 3.6, 0.9, 11.8),
    (Papa, 130, 2, 0.2, 30),
    (Salmón, 206, 22, 13.5, 0),
]

# Requisitos diarios del individuo (calorías, proteínas, grasas, carbohidratos)
requisitos = (2000, 150, 70, 300)

# Número de individuos en la población
num_individuos = 100

# Número máximo de generaciones
num_generaciones = 100

# Tamaño del torneo para selección de padres
tamano_torneo = 5

# Probabilidad de mutación
prob_mutacion = 0.2

def fitness(solucion, requisitos)
    
    Calcula la aptitud de una solución dada.
    
    calorias_consumidas = sum(a[1]cantidad for a, cantidad in zip(alimentos, solucion))
    proteinas_consumidas = sum(a[2]cantidad for a, cantidad in zip(alimentos, solucion))
    grasas_consumidas = sum(a[3]cantidad for a, cantidad in zip(alimentos, solucion))
    carbohidratos_consumidos = sum(a[4]cantidad for a, cantidad in zip(alimentos, solucion))

    diferencia_calorias = abs(calorias_consumidas - requisitos[0])
    diferencia_proteinas = abs(proteinas_consumidas - requisitos[1])
    diferencia_grasas = abs(grasas_consumidas - requisitos[2])
    diferencia_carbohidratos = abs(carbohidratos_consumidos - requisitos[3])

    return 1  (1 + diferencia_calorias + diferencia_proteinas + diferencia_grasas + diferencia_carbohidratos)

def inicializar_poblacion(num_individuos)
    
    Inicializa una población de individuos con soluciones aleatorias.
    
    return [[random.randint(0, 10) for _ in range(len(alimentos))] for _ in range(num_individuos)]

def seleccionar_padres(poblacion)
    
    Selecciona padres utilizando el método de torneo.
    
    padres = []
    for _ in range(len(poblacion))
        torneo = random.sample(poblacion, tamano_torneo)
        padres.append(max(torneo, key=lambda x fitness(x, requisitos)))
    return padres

def cruzar(padre1, padre2)
    
    Realiza el cruce de dos padres para producir un hijo.
    
    punto_cruce = random.randint(0, len(padre1) - 1)
    hijo = padre1[punto_cruce] + padre2[punto_cruce]
    return hijo

def mutar(solucion)
    
    Realiza una mutación en la solución.
    
    if random.random()  prob_mutacion
        gen_a_mutar = random.randint(0, len(solucion) - 1)
        solucion[gen_a_mutar] = random.randint(0, 10)

def generar_dieta()
    
    Genera una dieta que cumple con los requisitos.
    
    poblacion = inicializar_poblacion(num_individuos)

    for _ in range(num_generaciones)
        padres = seleccionar_padres(poblacion)

        nueva_poblacion = []
        for i in range(0, len(padres), 2)
            hijo1 = cruzar(padres[i], padres[i + 1])
            hijo2 = cruzar(padres[i + 1], padres[i])
            mutar(hijo1)
            mutar(hijo2)
            nueva_poblacion.extend([hijo1, hijo2])

        poblacion = nueva_poblacion

    mejor_solucion = max(poblacion, key=lambda x fitness(x, requisitos))

    return [(alimentos[i][0], mejor_solucion[i]) for i in range(len(alimentos))]

# Generar la dieta
dieta_generada = generar_dieta()
print(Dieta generada)
for alimento, cantidad in dieta_generada
    print(f{alimento} {cantidad} porciones)
