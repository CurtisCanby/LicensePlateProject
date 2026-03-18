import streamlit as st
import os

left, middle, right = st.columns(3)
right.page_link("main.py", label="Back ->", use_container_width=True)

left2, middle2, right2 = st.columns(3)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
images_path = os.path.join(BASE_DIR, "..", "images")

img_list = os.listdir(images_path)

#show images in the gallery, listing them in 3 columns
count = 0
for img in img_list:
    img_path = os.path.join(images_path, img)
    match count:
        case 0:
            left2.image(img_path)
            count += 1
        case 1:
            middle2.image(img_path)
            count += 1
        case 2:
            right2.image(img_path)
            count = 0