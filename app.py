import streamlit as st
import os
from PIL import Image

#Definition von Titel und Folder mit Grafiken
st.title("Bear Dataset Visualisierung")

image_folder = 'bear'

# Laden der Bilder
def load_images(image_folder):
    images = []
    for filename in os.listdir(image_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img_path = os.path.join(image_folder, filename)
            images.append(img_path)
    return images

# Bilder laden
image_paths = load_images(image_folder)

# Mit Slider darstellen wieviele Bilder vom gesamten Datenset gezeigt werden
st.subheader("Bilder des Bear-Datensatzes")
num_images = st.slider("Anzahl der anzuzeigenden Bilder", 1, len(image_paths), 5)
for img_path in image_paths[:num_images]:
    image = Image.open(img_path)
    st.image(image, caption=os.path.basename(img_path))

# Mit Slider entscheiden welches Bild angezeigt werden soll
st.subheader("Bilder Steuerung")
image_index = st.slider('Wählen Sie ein Bild aus', 0, len(image_paths) - 1, 0)
selected_image_path = image_paths[image_index]
st.image(selected_image_path, caption=os.path.basename(selected_image_path))


