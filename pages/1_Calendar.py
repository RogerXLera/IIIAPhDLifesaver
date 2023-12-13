"""
Roger Lera
09/12/2023
"""
import os
import numpy as np
import time
import csv
import streamlit as st


def switch_page(page_name: str):

    from streamlit.runtime.scriptrunner import RerunData,RerunException

    def standardize_name(name: str) -> str:
        return name.lower().replace("_", " ")
    
    page_name = standardize_name(page_name)

    pages = st.source_util.get_pages("Home.py")  # OR whatever your main page is called

    for page_hash, config in pages.items():
        if standardize_name(config["page_name"]) == page_name:
            raise RerunException(
                RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
                )
            )

    page_names = [standardize_name(config["page_name"]) for config in pages.values()]

    raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")

    return None

wd = 'documents'
path = os.getcwd()
    
st.write("# Welcome to the IIIA PhD Lifesaver! :ring_buoy: ")


st.markdown(
    """
    This app aims to gather all the important information a PhD might need during their PhD. 

    Important links:

        1. [UAB PhD Program](https://www.uab.cat/en/phds/computer-science).
        2. [SIA UAB](https://sia.uab.es/). Website where all bureacracy is done.
        3. [IIIA Intranet](https://iiia.csic.es/en-us/intranet/). 
    
    """
)

link_1 = st.button("Go to calendar.", disabled=False)
link_2 = st.button("Go to material.", disabled=False)

if link_1:
    switch_page("Calendar")
elif link_2:
    switch_page("Material")
