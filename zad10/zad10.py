#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plots = {"Histogram": "hist", "Box Plot": "box"}
st.header("PAD 10")
page = st.selectbox("Choose your page", ["Ankieta", "Staty"]) 

if page == "Ankieta":
    with st.form("my_form", True):
        st.write("Please enter your name and surname")
        name = st.text_input("Name")
        surname = st.text_input("Surname")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success(f"{name} {surname}")

if page == "Staty":
    data = st.file_uploader("Upload your csv file", type=['csv'])
    with st.spinner("Loading..."):
        if data:
            df = pd.read_csv(data)
            st.dataframe(df)
            plot = st.selectbox("Choose plot type", ["Histogram", "Box Plot"])
            selected_columns = st.multiselect("Select columns to plot", df.columns.to_list())
            plot_data = df[selected_columns]
            if selected_columns:
                fig = plot_data.plot(kind=plots[plot]).get_figure()
                st.pyplot(fig)
