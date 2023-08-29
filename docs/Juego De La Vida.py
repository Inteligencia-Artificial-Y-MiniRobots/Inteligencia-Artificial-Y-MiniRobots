import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Función para crear un tablero inicial aleatorio
def inicializar_tablero(N):
    tablero = np.random.randint(2, size=(N, N))
    return tablero

# Función para calcular el siguiente estado del tablero
def siguiente_estado(tablero):
    N = len(tablero)
    nuevo_tablero = np.copy(tablero)
    for i in range(N):
        for j in range(N):
            total_vecinos = int((tablero[i, (j-1)%N] + tablero[i, (j+1)%N] +
                                 tablero[(i-1)%N, j] + tablero[(i+1)%N, j] +
                                 tablero[(i-1)%N, (j-1)%N] + tablero[(i-1)%N, (j+1)%N] +
                                 tablero[(i+1)%N, (j-1)%N] + tablero[(i+1)%N, (j+1)%N]) / 1)
            if tablero[i, j] == 1:
                if (total_vecinos < 2) or (total_vecinos > 3):
                    nuevo_tablero[i, j] = 0
            else:
                if total_vecinos == 3:
                    nuevo_tablero[i, j] = 1
    return nuevo_tablero

# Función para animar el juego de la vida
def animar_juego(N, pasos):
    tablero = inicializar_tablero(N)
    fig, ax = plt.subplots()
    img = ax.imshow(tablero, interpolation='nearest')

    def actualizar(i):
        nonlocal tablero
        tablero = siguiente_estado(tablero)
        img.set_array(tablero)
        return img,

    animacion = animation.FuncAnimation(fig, actualizar, frames=pasos, interval=500)
    plt.show()

# Llama a la función para animar el juego de la vida
N = 100  # Tamaño del tablero
pasos = 100  # Número de generaciones
animar_juego(N, pasos)