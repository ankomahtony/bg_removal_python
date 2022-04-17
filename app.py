import streamlit as st
# import rembg
from rembg import remove
import io, os
from PIL import Image

st.title("Remove the backgroud of your Image")
image = st.file_uploader('Upload image',type=['png','jpeg','jpg','webp'])

col1, col2 = st.columns(2)

#function
def remove_bg(image):
    input_img = Image.open(image)
    result = remove(input_img)
    return result

if image:
    
    st.spinner()
    with st.spinner(text='Removing the background. Give it a sec...'):

        filename = image.name.split('.')[:-1]
        output =''.join(filename)+'_no_bg.png'
        new_image = remove_bg(image)
        new_image.save(output)
    
    
    col1.image(image)
    col2.image(new_image)

    with open(output, "rb") as file:

        btn = col2.download_button(

            label="Download",

            data=file,

            file_name=output,

            mime="image/png"

        )
        
        os.remove(output)

        



# st.write("Package: [rembg](https://github.com/danielgatis/rembg)")
    # download_image = Image.open()
    # col2.download_button(label="Download img",data=download_image,file_name=output,mime='image/png' )