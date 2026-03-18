import streamlit as st
import os
import LicensePlateReader as reader

left, middle, right = st.columns(3)
left.page_link("pages/gallery.py", label="Gallery", icon="📷", use_container_width=True)
right.button("Refresh", use_container_width=True)
st.markdown("""## :violet[License Plate Recognition]""")

#add any image file type you want the program to be able to accept
plates = st.file_uploader(
    "Upload Pictures", accept_multiple_files=True, type=["png", "jpg", "webp"]
)

#place holder for image we want to display
pic_container = st.empty()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "images")


left2, middle2, right2 = st.columns(3)
if middle2.button(label="Detect", use_container_width=True):
    if len(plates) != 0:

        #will loop through images as license plate detection code works through them
        for plate in plates:
            pic_container.image(plate)

        #save images to the images folder
        for plate in plates:
            destination_path = os.path.join(IMAGES_DIR, plate.name)
            with open(destination_path, "wb") as f:
                f.write(plate.getvalue())
            plate_text = reader.detect_plate_number(destination_path)
            # Show result
            st.success(f"Detected Plate ({plate.name}): {plate_text}")




# icons that can be used 📷 🔄 