import os
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from sklearn.model_selection import train_test_split

# Configuración
IMG_DIR = "ProyectoFinal/img_align_celeba"
ATTR_FILE = "ProyectoFinal/list_attr_celeba.csv"
IMG_SIZE = (128, 128)
BATCH_SIZE = 32
SELECTED_ATTRS = ['Smiling', 'Male', 'Young']

# Cargar atributos
df = pd.read_csv(ATTR_FILE)
df.set_index('image_id', inplace=True)
df = df[SELECTED_ATTRS]
df = df.replace(-1, 0)  # Convertir -1 a 0 para clasificación binaria

# Dividir en entrenamiento y validación
train_df, val_df = train_test_split(df, test_size=0.2, random_state=42)

# Función para cargar imágenes y etiquetas
def load_image_and_labels(image_id, label):
    image_id_str = image_id.numpy().decode('utf-8')  # Convertir tensor a string
    img_path = os.path.join(IMG_DIR, image_id_str)
    img = load_img(img_path, target_size=IMG_SIZE)
    img_array = img_to_array(img) / 255.0
    return img_array, label


# Convertir a tf.data.Dataset
def df_to_dataset(dataframe):
    image_ids = dataframe.index.values
    labels = dataframe.values.astype('float32')
    dataset = tf.data.Dataset.from_tensor_slices((image_ids, labels))

    def process(x, y):
        img, label = tf.py_function(load_image_and_labels, [x, y], [tf.float32, tf.float32])
        img.set_shape((128, 128, 3))  # Establecer forma explícita
        label.set_shape((len(SELECTED_ATTRS),))
        return img, label

    dataset = dataset.map(process, num_parallel_calls=tf.data.AUTOTUNE)
    dataset = dataset.batch(BATCH_SIZE).prefetch(tf.data.AUTOTUNE)
    return dataset


train_ds = df_to_dataset(train_df)
val_ds = df_to_dataset(val_df)

# Modelo CNN simple
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(128, 128, 3)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(len(SELECTED_ATTRS), activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entrenamiento
model.fit(train_ds, validation_data=val_ds, epochs=5)

