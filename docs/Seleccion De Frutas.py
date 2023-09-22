from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image
import numpy as np

training_dir = "archive/Testing"
testing_dir = "archive/Training"

# Crear generadores de imágenes
train_datagen = ImageDataGenerator(
    rescale=1./255,       # Normalizar los valores de píxeles
    shear_range=0.2,      # Aplicar transformaciones de inclinación aleatorias
    zoom_range=0.2,       # Aplicar transformaciones de zoom aleatorias
    horizontal_flip=True  # Voltear horizontalmente algunas imágenes aleatorias
)

test_datagen = ImageDataGenerator(rescale=1./255)

# Configurar generadores de flujo de datos
batch_size = 32

train_generator = train_datagen.flow_from_directory(
    training_dir,
    target_size=(64, 64),  # Redimensionar imágenes a 64x64 píxeles
    batch_size=batch_size,
    class_mode='categorical'
)

test_generator = test_datagen.flow_from_directory(
    testing_dir,
    target_size=(64, 64),
    batch_size=batch_size,
    class_mode='categorical'
)

# Crear un modelo secuencial
model = Sequential()

# Añadir capas convolucionales y de pooling
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Añadir capas completamente conectadas
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))  # Regularización para prevenir sobreajuste
model.add(Dense(4, activation='softmax'))  # 4 clases (manzanas, peras, bananos, fresas)

# Compilar el modelo
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Resumen del modelo
model.summary()

# Entrenar el modelo
history = model.fit(
    train_generator,
    steps_per_epoch=len(train_generator),
    epochs=10,
    validation_data=test_generator,
    validation_steps=len(test_generator)
)

# Evaluar el rendimiento del modelo
loss, accuracy = model.evaluate(test_generator, steps=len(test_generator))
print(f'Precisión en el conjunto de prueba: {accuracy * 100:.2f}%')

# Visualizar la pérdida y precisión durante el entrenamiento
plt.plot(history.history['loss'], label='Pérdida de entrenamiento')
plt.plot(history.history['val_loss'], label='Pérdida de validación')
plt.xlabel('Épocas')
plt.ylabel('Pérdida')
plt.legend()
plt.show()

plt.plot(history.history['accuracy'], label='Precisión de entrenamiento')
plt.plot(history.history['val_accuracy'], label='Precisión de validación')
plt.xlabel('Épocas')
plt.ylabel('Precisión')
plt.legend()
plt.show()


# Función para cargar y preprocesar una imagen nueva
def cargar_y_preprocesar_imagen(ruta):
    img = image.load_img(ruta, target_size=(64, 64))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0  # Normalizar valores de píxeles
    return img

# Ruta de la nueva imagen de fruta
ruta_nueva_imagen = "archive/Testing/Apple/3_100.jpg"

# Cargar y preprocesar la nueva imagen
nueva_imagen = cargar_y_preprocesar_imagen(ruta_nueva_imagen)

# Realizar la predicción
prediccion = model.predict(nueva_imagen)

# Obtener la clase predicha
clase_predicha = np.argmax(prediccion)

# Asociar el índice de clase con el nombre de la fruta
clases = ["apple", "pear", "banana", "strawberry"]
fruta_predicha = clases[clase_predicha]

# Mostrar el resultado
print(f"La fruta predicha es: {fruta_predicha}")
