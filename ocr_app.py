import easyocr
import streamlit as st
from PIL import Image


def perform_ocr(image):
    reader = easyocr.Reader(['en', 'hi'])
    result = reader.readtext(image, detail=0)
    return" ".join(result)

# Streamlit


def main():
    st.title("OCR App: Extract Text from Images")

    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_image:
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        text = perform_ocr(uploaded_image)
        st.write("Extracted Text:")
        st.write(text)

        keyword = st.text_input("Enter a keyword to search:")
        if keyword:
            if keyword in text:
                st.write(f"'{keyword}' found in the text.")
            else:
                st.write(f"'{keyword}' not found in the text.")

    if __name__ == "__main__":
        main()
