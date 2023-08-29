import cv2
import numpy as np

# Cargamos la imagen desde Google Drive
ruta_imagen = 'images/fallguys.png'

# Carga la imagen a color
imagen_color = cv2.imread(ruta_imagen)

# Verifica si la carga fue exitosa
if imagen_color is not None:
    print("Imagen cargada exitosamente.")
else:
    print("No se pudo cargar la imagen.")

# Convierte la imagen a escala de grises
imagen_gris = cv2.cvtColor(imagen_color, cv2.COLOR_BGR2GRAY)

# Obtiene las dimensiones de la imagen en escala de grises
alto, ancho = imagen_gris.shape

# Diccionario para almacenar las reglas de asignación de color
reglas_asignacion = {}

# Recorre la imagen en escala de grises y obtiene las reglas de asignación
for i in range(1, alto - 1):
    for j in range(1, ancho - 1):
        pixel_gris = imagen_gris[i, j]

        # Vecindad de Moore de 9 vecinos
        vecinos_gris = [
            imagen_gris[i - 1, j - 1], imagen_gris[i - 1, j], imagen_gris[i - 1, j + 1],
            imagen_gris[i, j - 1], pixel_gris, imagen_gris[i, j + 1],
            imagen_gris[i + 1, j - 1], imagen_gris[i + 1, j], imagen_gris[i + 1, j + 1]
        ]

        vecinos_color = [
            imagen_color[i - 1, j - 1], imagen_color[i - 1, j], imagen_color[i - 1, j + 1],
            imagen_color[i, j - 1], imagen_color[i, j], imagen_color[i, j + 1],
            imagen_color[i + 1, j - 1], imagen_color[i + 1, j], imagen_color[i + 1, j + 1]
        ]

        # Calcula la regla de asignación de color basada en la vecindad de Moore
        regla_color = np.mean(vecinos_color, axis=0).astype(int)
        reglas_asignacion[pixel_gris] = regla_color

# Crea una nueva imagen en color utilizando las reglas de asignación
imagen_color_generada = np.zeros_like(imagen_color)

for i in range(alto):
    for j in range(ancho):
        pixel_gris = imagen_gris[i, j]
        color_asignado = reglas_asignacion[pixel_gris]
        imagen_color_generada[i, j] = color_asignado

# Muestra la imagen original y la imagen generada
cv2.imshow('Imagen Original', imagen_color)
cv2.imshow('Imagen Generada', imagen_color_generada)
cv2.waitKey(0)
cv2.destroyAllWindows()