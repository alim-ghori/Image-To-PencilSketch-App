import streamlit as st
import numpy as np
from PIL import Image
import cv2


def dodgeV2(x, y):
    return cv2.divide(x, 255 - y, scale=256)


def pencilsketch(inp_img):
    img_gray = cv2.cvtColor(inp_img, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_smooting = cv2.GaussianBlur(img_invert, (21, 21), sigmaX=0, sigmaY=0)
    final_img = dodgeV2(img_gray, img_smooting)
    return(final_img)


st.title("Image to Pencil-Sketch App")
st.write("Web app is to convert image to realistic Pencil Sketch")

file_image = st.camera_input(label="Take a picture to be sketch out")

if file_image:
    input_img = Image.open(file_image)
    final_sketch = pencilsketch(np.array(input_img))
    one, two = st.columns(2)
    with one:
        st.write("**input Photo**\n")
        st.image(input_img, use_column_width=True)
    with two:
        st.write("**Output Pencil Sketch**")
        st.image(final_sketch, use_column_width=True)
    if st.button("Download Sketch Image"):
        im_pil = image.fromarray(final_sketch)
        im_pil.save('final_image.jpeg')
        st.write('Download completed')

else:
    st.write("you hane not uploaded any image file... Please upload one!")
