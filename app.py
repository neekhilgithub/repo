#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import leafmap
import streamlit as st
from samgeo import tms_to_geotiff

def download_google_data():
    st.title("Google Data Downloader")

    # Specify a Google basemap to use
    basemap_choice = st.selectbox("Select a Google basemap", ["ROADMAP", "TERRAIN", "SATELLITE", "HYBRID"])

    # Prompt the user to enter bounding box information
    st.subheader("Enter the bounding box information")
    bbox_input = st.text_input("Bounding Box (xmin, ymin, xmax, ymax)", "-51.253043,-22.17615,-51.2498,-22.1739")
    bbox = [float(coord.strip()) for coord in bbox_input.split(',')]

    # Prompt the user to enter the file name for the image
    output_filename = st.text_input("Enter the file name for the image (without extension)", "output")

    # State variable to keep track of download success
    if 'download_success' not in st.session_state:
        st.session_state.download_success = False

    # Convert TMS to GeoTIFF image
    if st.button("Download GeoTIFF"):
        st.write("Please wait...")
        try:
            tms_to_geotiff(output=output_filename + ".tif", bbox=bbox, zoom=19, source=basemap_choice, overwrite=True)
            st.session_state.download_success = True
            st.write("Download successful!")
        except Exception as e:
            st.error(f"Error: {e}")

    # Display the "Show GeoTIFF" button only if download was successful
    if st.session_state.download_success:
        if st.button("Show GeoTIFF"):
            st.image(output_filename + ".tif")

if __name__ == "__main__":
    download_google_data()
