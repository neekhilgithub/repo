#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
from samgeo.text_sam import LangSAM

def main():
    st.title('Image Processing with LangSAM')

    # Get input image path from user
    image_path = st.text_input("Enter the path to the input image: ")

    # Get text prompt from user
    text_prompt = st.text_area("Enter the text prompt: ")
    
    box_threshold = st.slider("Enter the box_threshold:", min_value=0.0, max_value=1.0, step=0.01)
    
    text_threshold = st.slider("Enter the text_threshold:", min_value=0.0, max_value=1.0, step=0.01)

    # Define output filename for raster
    output_filename = st.text_input("Enter the output filename for raster (without extension): ", value="output").strip()

    # Define output filename for vector
    output_vector_filename = st.text_input("Enter the output filename for vector (without extension): ", value="vector").strip()

    if st.button("Process"):
        try:
            # Initialize LangSAM model
            sam = LangSAM()

            # Predict using LangSAM model
            sam.predict(image_path, text_prompt, box_threshold, text_threshold)

            # Show annotations
            sam.show_anns(
                cmap='Greys_r',
                add_boxes=False,
                alpha=1,
                title='Automatic Segmentation',
                blend=False,
                output=output_filename + '.tif',  # Using the defined output filename
            )

            # Convert raster to vector
            sam.raster_to_vector(output_filename + ".tif", output_vector_filename + ".shp")

            st.success("Processing completed successfully.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()

